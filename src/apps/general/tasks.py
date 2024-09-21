import requests
from django.core.cache import cache
from celery import shared_task


@shared_task
def get_currency():
    response = requests.get('https://cbu.uz/oz/arkhiv-kursov-valyut/json/')
    usd_and_sum = response.json()[0]['Rate']
    cache.set('usd_and_sum', usd_and_sum, timeout=60 * 60 * 24)
