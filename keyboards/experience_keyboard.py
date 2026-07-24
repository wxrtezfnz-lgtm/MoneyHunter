from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

experience_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🟢 Полный новичок")],
        [KeyboardButton(text="🟡 Уже пробовал")],
        [KeyboardButton(text="🔵 Уже зарабатываю")]
    ],
    resize_keyboard=True
)