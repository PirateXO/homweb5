import asyncio
import sys
from currency_checker.currency_service import CurrencyService
from currency_checker.logger import Logger

async def main():
    if len(sys.argv) < 2:
        print("Usage: py main.py <days> [currencies...]")
        return

    try:
        days = int(sys.argv[1])
        if days > 10:
            print("Error: You can only request up to 10 days.")
            return

        currencies = sys.argv[2:] if len(sys.argv) > 2 else None
        currency_service = CurrencyService(days, currencies)

        # Fetch currency data
        currency_data = await currency_service.get_currency_data()
        print(currency_data)

        # Log the command
        await Logger.log_to_file(f"Checked exchange rates for {days} days and currencies {currencies or 'USD, EUR'}")

    except ValueError:
        print("Please provide a valid number of days.")

if __name__ == '__main__':
    asyncio.run(main())
