import requests

from django.conf import settings
from django.core.cache import cache
import random


class EskizUz:
    TOKEN_KEY = "eskiz_uz_token"
    AUTH_CODE_KEY = "auth_code_{phone_number}"

    FORGOT_PASSWORD_KEY = 'forgot_token_password{token}'

    GET_TOKEN_URL = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"
    SEND_SMS_URL = "YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY"

    FORGOT_PASSWORD_MESSAGE = "Follow the link below to reset your password {link}"
    AUTH_CODE_MESSAGE = "{code}"

    EMAIL = settings.ESKIZ_UZ_EMAIL
    PASSWORD = settings.ESKIZ_UZ_PASSWORD

    @classmethod
    def get_token(cls):
        token = cache.get(cls.TOKEN_KEY)
        if not token:
            response = requests.post(
                url=cls.GET_TOKEN_URL,
                data={
                    'email': cls.EMAIL,
                    'password': cls.PASSWORD
                }
            )
            token = response.json()['data']['token']
            cache.set(cls.TOKEN_KEY, token, timeout=60 * 60 * 24 * 29)
        return token

    @classmethod
    def send_sms(cls, send_type: str, phone_number: str, nickname='4546', link=None, forgot_id=None):
        if send_type == 'FORGOT_PASSWORD':
            message = cls.FORGOT_PASSWORD_MESSAGE.format(link=link)
            cache.set(f'forgot_id_password_{phone_number}', forgot_id, timeout=60 * 10)

        elif send_type == 'AUTH_CODE':
            code = random.randint(1000, 9999)
            message = cls.AUTH_CODE_MESSAGE.format(code=code)
            cache.set(cls.AUTH_CODE_KEY.format(phone_number=phone_number), code, 60 * 10)
        else:
            raise ValueError("Invalid send type")

        return message
