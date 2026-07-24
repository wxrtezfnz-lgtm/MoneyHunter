from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

goal_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💰 Начать зарабатывать")],
        [KeyboardButton(text="🤖 Освоить ИИ")],
        [KeyboardButton(text="📈 Построить бизнес")],
        [KeyboardButton(text="🚀 Пока не знаю")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выбери свою цель 👇",
)