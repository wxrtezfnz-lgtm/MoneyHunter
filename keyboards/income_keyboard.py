from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

income_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💵 До 50 000 ₽")],
        [KeyboardButton(text="💸 50–100 тыс. ₽")],
        [KeyboardButton(text="🚀 100–300 тыс. ₽")],
        [KeyboardButton(text="👑 Более 300 тыс. ₽")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выбери желаемый доход 👇"
)