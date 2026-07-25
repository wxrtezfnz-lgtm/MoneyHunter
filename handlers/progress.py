from aiogram import Router
from aiogram.types import CallbackQuery

from database.db import get_day, next_day

router = Router()


@router.callback_query(lambda c: c.data == "next_day")
async def next_day_callback(callback: CallbackQuery):

    next_day(callback.from_user.id)

    day = get_day(callback.from_user.id)

    progress = min(day * 10, 100)

    bars = "█" * (progress // 10) + "░" * (10 - progress // 10)

    await callback.message.edit_text(
        f"🎉 <b>Отличная работа!</b>\n\n"

        f"🔥 День <b>{day}</b> из 30\n\n"

        f"{bars} {progress}%\n\n"

        "Продолжай в том же духе 🚀",

        parse_mode="HTML"
    )

    await callback.answer("Прогресс сохранён ✅")