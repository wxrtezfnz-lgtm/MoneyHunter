from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏠 Главная"),
            KeyboardButton(text="👤 Профиль")
        ],
        [
            KeyboardButton(text="🎯 Моё задание"),
            KeyboardButton(text="🏆 Достижения")
        ],
        [
            KeyboardButton(text="⚙️ Настройки")
        ]
    ],
    resize_keyboard=True
)