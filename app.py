from aiogram import Router, F
from aiogram.types import Message

from database.db import get_profile, get_achievements
from services.achievements import ACHIEVEMENTS

router = Router()


@router.message(F.text == "👤 Профиль")
async def profile(message: Message):

    user = get_profile(message.from_user.id)

    if not user:
        await message.answer(
            "Сначала пройди регистрацию через /start 😊"
        )
        return

    xp = user["xp"]
    level = user["level"]

    current_level_xp = (level - 1) * 100
    next_level_xp = level * 100

    progress = xp - current_level_xp
    need = next_level_xp - current_level_xp

    bars = int((progress / need) * 10)
    bars = max(0, min(10, bars))

    bar = "█" * bars + "░" * (10 - bars)

    await message.answer(

        f"👤 <b>{user['name']}</b>\n\n"

        f"⭐️ <b>Уровень {level}</b>\n"

        f"⚡️ XP: <b>{xp}</b>\n"
        f"{bar} {progress}/{need}\n\n"

        f"🔥 Серия: <b>{user['streak']}</b>\n"
        f"🏆 Достижения: <b>{len(get_achievements(message.from_user.id))}</b>\n"
        f"📅 День курса: <b>{user['day']}/30</b>\n\n"

        f"🎯 Цель: {user['goal']}\n"
        f"💰 Доход: {user['income']}\n"
        f"🧠 Опыт: {user['experience']}",

        parse_mode="HTML"
    )


@router.message(F.text == "🏠 Главная")
async def home(message: Message):

    await message.answer(
        "🏠 Добро пожаловать обратно!"
    )


@router.message(F.text == "🎯 Моё задание")
async def task(message: Message):

    await message.answer(
        "🎯 Скоро здесь будет открываться текущее задание."
    )


@router.message(F.text == "🏆 Достижения")
async def achievements(message: Message):

    opened = get_achievements(message.from_user.id)

    text = "🏆 <b>Достижения</b>\n\n"

    for key, value in ACHIEVEMENTS.items():

        if key in opened:
            text += f"🟢 {value['title']}\n"
        else:
            text += f"⚪ {value['title']}\n"

    await message.answer(
        text,
        parse_mode="HTML"
    )


@router.message(F.text == "⚙️ Настройки")
async def settings(message: Message):

    await message.answer(
        "⚙️ Настройки пока находятся в разработке."
    )