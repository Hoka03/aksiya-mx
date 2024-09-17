import random

from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.password_validation import validate_password
from django.core.cache import cache

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.authentications.sms_providers import EskizUz
from apps.users.validations import phone_validate


class SendAuthCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, validators=[phone_validate])
    code = serializers.IntegerField(read_only=True)

    @staticmethod
    def send_code(phone_number, code):
        print(f'Code {code} sent to {phone_number}.')

    @staticmethod
    def generate_code():
        return random.randint(1000, 9999)

    def validate_phone_number(self, phone_number):
        if get_user_model().objects.filter(phone_number=phone_number).exists():
            raise ValidationError('Such a phone number was not found.')
        return phone_number

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number = attrs['phone_number']
        attrs['code'] = self.generate_code()
        self.send_code(phone_number, attrs['code'])
        cache.set(f'{phone_number}_auth_code', attrs['code'], 10 * 60)

        return attrs


class VerifyCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, validators=[phone_validate], write_only=True)
    code = serializers.IntegerField(write_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)

        phone_number, code = attrs['phone_number'], attrs['code']
        if cache.get(f"{phone_number}_auth_code") != self.code:
            raise ValidationError('Code was entered mistake.')

        return attrs


class RegisterSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=13, validators=[phone_validate])
    password = serializers.CharField(max_length=100, write_only=True, validators=[validate_password])
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)

        phone_number, password = attrs['phone_number'], attrs['password']

        user = get_user_model().objects.create_user(phone_number=phone_number, password=password)

        #   Generate JWT Token
        refresh_token = RefreshToken.for_user(user)
        attrs['access_token'] = str(refresh_token.access_token)
        attrs['refresh_token'] = str(refresh_token)

        cache.delete(f"{phone_number}_auth_code")

        return attrs


class ForgotPasswordSerializer(serializers.Serializer):
    def validate_phone_number(self, phone_number):
        if not get_user_model().objects.filter(phone_number=phone_number).exists():
            raise ValidationError("User with this phone number does not exist.")
        return phone_number

    def save(self, *args, **kwargs):
        """
        Send forgot password link to phone number user.
        """
        forgot_id = random.randint(1000, 9999)
        link = self.context['request'].build_absolute_uri(f'new_password/?forgot_id={forgot_id}')
        EskizUz.send_sms(
            send_type='FORGOT_PASSWORD',
            phone_number=self.validated_data['phone_number'],
            link=link
        )

        self.validated_data['link'] = link

        cache.set(f'forgot_id={forgot_id}', self.validated_data['phone_number'], timeout=60 * 10)


class NewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100, validators=[validate_password], write_only=True)
    refresh_token = serializers.CharField(read_only=True)
    access_token = serializers.CharField(read_only=True)

    def save(self, **kwargs):
        attrs = self.validated_data
        context = self.context

        phone_number, forgot_id = context['phone_number'], context['forgot_id']

        user = get_user_model().objects.get(phone_number=phone_number)
        user.set_password(attrs['password'])
        user.save()

        cache.delete(f'forgot_id={forgot_id}')

        refresh = RefreshToken.for_user(user)
        attrs['refresh_token'] = str(refresh)
        attrs['access_token'] = str(refresh.access_token)