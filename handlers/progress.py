from aiogram import Router
from aiogram.types import CallbackQuery

from database.db import get_day, next_day
from services.day_builder import build_day
from keyboards.progress_keyboard import progress_keyboard

router = Router()


@router.callback_query(lambda c: c.data == "next_day")
async def next_day_callback(callback: CallbackQuery):

    day = get_day(callback.from_user.id)

    # если курс уже закончен
    if day >= 30:
        await callback.message.edit_text(
            "🏆 <b>Поздравляю!</b>\n\n"
            "Ты полностью прошёл 30-дневный путь Money Hunter.\n\n"
            "🚀 Теперь ты готов брать первые проекты и масштабировать доход.",
            parse_mode="HTML"
        )

        await callback.answer("Курс завершён 🎉")
        return

    # увеличиваем день
    next_day(callback.from_user.id)

    day = get_day(callback.from_user.id)

    progress = int(day / 30 * 100)

    bars = "█" * (progress // 10) + "░" * (10 - progress // 10)

    await callback.message.edit_text(
        f"🎉 <b>Отличная работа!</b>\n\n"
        f"🔥 День <b>{day}</b> из 30\n\n"
        f"{bars} {progress}%\n\n"
        "Продолжай в том же духе 🚀",
        parse_mode="HTML"
    )

    await callback.message.answer(
        build_day(day),
        parse_mode="HTML",
        reply_markup=progress_keyboard if day < 30 else None
    )

    await callback.answer("Прогресс сохранён ✅")