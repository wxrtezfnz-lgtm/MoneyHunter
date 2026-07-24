from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

activity_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🎓 Учусь")],
        [KeyboardButton(text="💼 Работаю")],
        [KeyboardButton(text="🔍 Ищу работу")],
        [KeyboardButton(text="🚀 Свой бизнес")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выбери вариант 👇",
)