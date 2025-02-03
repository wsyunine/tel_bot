import asyncio
import telegram


async def main():
    bot = telegram.Bot("7653536587:AAG7Tskt2zfDrRcLNMFjKi33pWGSa51QqSE")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())
