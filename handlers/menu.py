
from aiogram.types import Message
from aiogram import Router, F

router = Router()


@router.message(lambda m: m.text == "🏠 Главная")
async def home(message: Message):
    await message.answer(
        "🏠 Главная\n\n"
        "Добро пожаловать обратно!"
    )


from database.db import get_profile


@router.message(F.text == "👤 Профиль")
async def profile(message: Message):

    user = get_profile(message.from_user.id)

    if not user:
        await message.answer(
            "Сначала пройди регистрацию через /start 😊"
        )
        return

    await message.answer(

        f"👤 <b>{user['name']}</b>\n\n"

        f"⭐ Уровень: <b>{user['level']}</b>\n"
        f"⚡ XP: <b>{user['xp']}</b>\n"
        f"🔥 Серия: <b>{user['streak']}</b>\n"
        f"🏆 Достижения: <b>{user['achievements']}</b>\n"
        f"📅 День курса: <b>{user['day']}/30</b>\n\n"

        f"🎯 Цель: {user['goal']}\n"
        f"💰 Доход: {user['income']}\n"
        f"🧠 Опыт: {user['experience']}",

        parse_mode="HTML"
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