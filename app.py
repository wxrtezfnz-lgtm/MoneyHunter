import asyncio
import os

print("1")

from aiogram import Bot, Dispatcher

print("2")

from dotenv import load_dotenv

print("3")

from handlers.start import router as start_router

print("4")

from handlers.progress import router as progress_router

print("5")

from handlers.menu import router as menu_router

print("6")

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

print("7")

bot = Bot(token=TOKEN)

print("8")

dp = Dispatcher()

print("9")

dp.include_router(start_router)

print("10")

dp.include_router(progress_router)

print("11")

dp.include_router(menu_router)

print("12")


async def main():
    print("✅ Бот запущен")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())