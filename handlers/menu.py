from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message(lambda m: m.text == "🏠 Главная")
async def home(message: Message):
    await message.answer(
        "🏠 Главная\n\n"
        "Добро пожаловать обратно!"
    )


@router.message(lambda m: m.text == "👤 Профиль")
async def profile(message: Message):
    await message.answer(
        "👤 Профиль\n\n"
        "Пока находится в разработке."
    )


@router.message(lambda m: m.text == "🎯 Моё задание")
async def task(message: Message):
    await message.answer(
        "🎯 Здесь будет текущее задание."
    )


@router.message(lambda m: m.text == "🏆 Достижения")
async def achievements(message: Message):
    await message.answer(
        "🏆 Здесь будут достижения."
    )


@router.message(lambda m: m.text == "⚙️ Настройки")
async def settings(message: Message):
    await message.answer(
        "⚙️ Настройки пока находятся в разработке."
    )