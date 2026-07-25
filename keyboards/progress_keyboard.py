from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

progress_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="✅ Выполнил задание",
                callback_data="next_day"
            )
        ]
    ]
)