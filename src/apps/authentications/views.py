from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, GenericAPIView

from django.core.cache import cache

from apps.authentications import serializers
from apps.authentications.serializers import NewPasswordSerializer
from apps.authentications.sms_providers import EskizUz


class ForgotPasswordAPIView(CreateAPIView):
    """
    This view is used to send a forgot password for phone number of user.
    """
    permission_classes = ()
    authentication_classes = ()

    serializer_class = serializers.ForgotPasswordSerializer


class NewPasswordAPIView(GenericAPIView):
    """
    This view is set new password to phone number of user.
    """
    queryset = []

    permission_classes = ()
    authentication_classes = ()

    serializer_class = NewPasswordSerializer

    def get(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        token_in_cache = cache.get(EskizUz.FORGOT_PASSWORD_KEY.format(token=token))
        if not token_in_cache:
            return Response({'error': 'request not found'}, status=404)
        return Response(status=200)

    def post(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        serializer = self.get_serializer(data=request.data,
                                         context={'token':token,})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class SendCodeAPIView(CreateAPIView):
    """
    This view is used to send code for that phone_number of user.
    """
    permission_classes = ()
    authentication_classes = ()

    serializer_class = serializers.SendAuthCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=200)


class VerifyCodeAPIView(CreateAPIView):
    """
    This view is used for verify code of user.
    """
    permission_classes = ()
    authentication_classes = ()

    serializer_class = serializers.VerifyCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=200)


class RegisterAPIView(CreateAPIView):
    permission_classes = ()
    authentication_classes = ()

    serializer_class = serializers.RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)