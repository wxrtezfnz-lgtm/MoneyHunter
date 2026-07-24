from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🚀 Добро пожаловать в Money Hunter AI!\n\n"
        "Я помогу тебе найти путь к первым деньгам.\n\n"
        "Пока это первая версия, но скоро я научусь составлять персональный план заработка."
    )