from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Добро пожаловать в Money Hunter AI.\n\n"
        "Напиши, как тебя зовут? 😊"
    )


@router.message()
async def echo(message: Message):
    await message.answer(
        f"Ты написал:\n\n{message.text}"
    )