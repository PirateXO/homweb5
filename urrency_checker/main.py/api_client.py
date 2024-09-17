import aiohttp
import asyncio

class ApiClient:
    @staticmethod
    async def fetch_currency_data(url):
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        return None
            except aiohttp.ClientError as e:
                print(f"Error fetching data: {e}")
                return None
