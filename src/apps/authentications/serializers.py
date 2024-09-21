import random

from django.contrib.auth.password_validation import validate_password
from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from pycparser.ply.yacc import token

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.authentications.jwt_validate import generate_token_jwt
from apps.authentications.sms_providers import EskizUz
from apps.users.validations import phone_validate


class SendAuthCodeSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=13, validators=[phone_validate])
    code = serializers.IntegerField(read_only=True)

    def validate_username(self, phone_number):
        if get_user_model().objects.filter(phone_number=phone_number).exists():
            raise ValidationError('Such a phone number was already exists.')
        return phone_number

    @classmethod
    def check_limit(cls, request):
        """
        Count how many times the one phone_number has requested the code
        """
        ip_address = request.META.get('REMOTE_ADDR')

        limit = cache.get(ip_address, 0)
        if limit >= 3:
            raise ValidationError('Try after one hour.')
        else:
            cache.set(ip_address, limit + 1, 60 * 60)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        self.check_limit(self.context['request'])
        return attrs

    def save(self, *args, **kwargs):
        """
        Send code to phone_number of user.
        """
        code = EskizUz.send_sms(
            send_type='AUTH_CODE',
            phone_number=self.validated_data['username']
        )

        self.validated_data['code'] = code


class VerifyCodeSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[phone_validate])
    code = serializers.IntegerField()

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, code = attrs['username'], attrs['code']

        if cache.get(EskizUz.AUTH_CODE_KEY.format(phone_number=phone_number)
                     ) != code:
            raise ValidationError('Code was entered mistake.')

        return attrs


class RegisterSerializer(VerifyCodeSerializer):
    """
    Here we are creating user and returning JWT TOKEN.
    """

    password = serializers.CharField(max_length=100, write_only=True, validators=[validate_password])
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)

        phone_number, password = attrs['username'], attrs['password']

        self.user_data = {
            'phone_number': phone_number,
            'password': password
        }

        return attrs


    def create(self, validated_data):
        # Create user here in the create method

        phone_number = self.user_data['phone_number']
        password = self.user_data['password']

        user = get_user_model().objects.create_user(phone_number=phone_number, password=password)

        # Clear cache for the verification code
        cache.delete(EskizUz.AUTH_CODE_KEY.format(phone_number=phone_number))

        # Generate JWT Token
        jwt_token = generate_token_jwt(user)

        validated_data['access_token'] = jwt_token['access_token']
        validated_data['refresh_token'] = jwt_token['refresh_token']

        return validated_data

class ForgotPasswordSerializer(serializers.Serializer):
    """
    here we give password for stupid people new password.
    """
    username = serializers.CharField(validators=[phone_validate])
    link = serializers.CharField(read_only=True)

    def validate_username(self, phone_number):
        if not get_user_model().objects.filter(phone_number=phone_number).exists():
            raise ValidationError("User with this phone number does not exist.")
        return phone_number


    def save(self, *args, **kwargs):
        """
        Send forgot password link to phone number user.
        """

        SendAuthCodeSerializer.check_limit(self.context['request'])

        user = get_object_or_404(get_user_model(), phone_number=self.validated_data['username'])
        token_generate = PasswordResetTokenGenerator()
        token = token_generate.make_token(user)
        link = self.context['request'].build_absolute_uri(f'confirm/?token-generate={token}')
        EskizUz.send_sms(
            send_type='FORGOT_PASSWORD',
            phone_number=self.validated_data['username'],
            link=link
        )

        self.validated_data['link'] = link


class NewPasswordSerializer(serializers.Serializer):
    """
    here we here give password after ForgotPasswordSerializer.
    """
    password = serializers.CharField(max_length=100, validators=[validate_password], write_only=True)
    username = serializers.CharField(validators=[phone_validate])

    refresh_token = serializers.CharField(read_only=True)
    access_token = serializers.CharField(read_only=True)

    def save(self, **kwargs):
        attrs = self.validated_data
        context = self.context

        # token = context['token']

        phone_number = cache.get(EskizUz.FORGOT_PASSWORD_KEY.format(token=token))
        if not phone_number:
            raise ValidationError('user not found.')

        user = get_object_or_404(get_user_model(), phone_number=phone_number)
        user.set_password(attrs['password'])
        user.save()

        cache.delete(EskizUz.FORGOT_PASSWORD_KEY.format(token=token))

        #   Generate JWT token
        jwt_token = generate_token_jwt(user)

        self.validated_data['access_token'] = jwt_token['access_token']
        self.validated_data['refresh_token'] = jwt_token['refresh_token']