from aiogram import Router, F
from aiogram.types import Message

from database.db import get_profile

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

    if bars > 10:
        bars = 10

    if bars < 0:
        bars = 0

    bar = "█" * bars + "░" * (10 - bars)

    await message.answer(

        f"👤 <b>{user['name']}</b>\n\n"

        f"⭐️ <b>Уровень {level}</b>\n"

        f"⚡️ XP: <b>{xp}</b>\n"
        f"{bar} {progress}/{need}\n\n"

        f"🔥 Серия: <b>{user['streak']}</b>\n"
        f"🏆 Достижения: <b>{user['achievements']}</b>\n"
        f"📅 День курса: <b>{user['day']}/30</b>\n\n"

        f"🎯 Цель: {user['goal']}\n"
        f"💰 Доход: {user['income']}\n"
        f"🧠 Опыт: {user['experience']}",

        parse_mode="HTML"
    )