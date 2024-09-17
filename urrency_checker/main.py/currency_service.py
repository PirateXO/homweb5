from datetime import datetime, timedelta
from .api_client import ApiClient
from .constants import BASE_URL, ALLOWED_CURRENCIES

class CurrencyService:
    def __init__(self, days, currencies):
        self.days = days
        self.currencies = currencies if currencies else ALLOWED_CURRENCIES

    def get_dates(self):
        today = datetime.now()
        dates = [(today - timedelta(days=i)).strftime('%d.%m.%Y') for i in range(self.days)]
        return dates

    async def get_currency_data(self):
        dates = self.get_dates()
        tasks = [self.fetch_and_format_data(date) for date in dates]
        results = await asyncio.gather(*tasks)
        return [result for result in results if result]

    async def fetch_and_format_data(self, date):
        url = f"{BASE_URL}{date}"
        data = await ApiClient.fetch_currency_data(url)
        if not data:
            return None

        return {
            date: {currency: self.extract_currency_data(data, currency) for currency in self.currencies}
        }

    def extract_currency_data(self, data, currency):
        for rate in data['exchangeRate']:
            if rate['currency'] == currency:
                return {
                    'sale': rate['saleRate'],
                    'purchase': rate['purchaseRate']
                }
        return None
