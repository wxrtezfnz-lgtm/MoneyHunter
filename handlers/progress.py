from aiogram import Router
from aiogram.types import CallbackQuery

from database.db import get_day, next_day

from keyboards.progress_keyboard import progress_keyboard
from services.day_builder import build_day

router = Router()


@router.callback_query(lambda c: c.data == "next_day")
async def next_day_callback(callback: CallbackQuery):

    # увеличиваем день
    next_day(callback.from_user.id)

    day = get_day(callback.from_user.id)

    # прогресс из 30 дней
    progress = int(day / 30 * 100)

    filled = progress // 10

    bars = "█" * filled + "░" * (10 - filled)

    # обновляем прошлое сообщение
    await callback.message.edit_text(
        f"🎉 <b>Отличная работа!</b>\n\n"
        f"🔥 День <b>{day}</b> из 30\n\n"
        f"{bars} {progress}%\n\n"
        "Продолжай в том же духе 🚀",
        parse_mode="HTML"
    )

    # сразу отправляем новое задание
    await callback.message.answer(
        build_day(day),
        parse_mode="HTML",
        reply_markup=progress_keyboard
    )

    await callback.answer("Прогресс сохранён ✅")