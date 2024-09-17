import aiofiles
import datetime

class Logger:
    @staticmethod
    async def log_to_file(message):
        log_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        async with aiofiles.open("exchange_log.txt", "a") as log_file:
            await log_file.write(f"[{log_time}] {message}\n")
