import requests
from celery import shared_task
from django.utils import timezone
from apps.general.models import CurrencyRate
from apps.discounts.choices import Currency


@shared_task
def update_usd_rate():
    url = 'https://cbu.uz/ru/arkhiv-kursov-valyut/json/'
    response = requests.get(url)
    data = response.json()

    try:
        usd_rate = next(item['Rate'] for item in data if item['Ccy'] == 'USD')
        usd_rate = float(usd_rate.replace(',', '.'))

        # Update or create the CurrencyRate object for USD
        CurrencyRate.objects.update_or_create(
            currency=Currency.USD,  # Assuming USD is represented by a value in Currency choices
            defaults={'in_sum': usd_rate}
        )

        print(f"USD rate updated to {usd_rate} at {timezone.now()}")

    except (IndexError, KeyError, ValueError) as e:
        print(f"Error updating USD rate: {e}")
