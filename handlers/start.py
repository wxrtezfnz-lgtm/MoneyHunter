from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.user_state import UserState

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Добро пожаловать в Money Hunter AI.\n\n"
        "Напиши, как тебя зовут? 😊"
    )

    await state.set_state(UserState.waiting_for_name)

@router.message(UserState.waiting_for_name)
async def get_name(message: Message, state: FSMContext):
    await message.answer(
        f"Приятно познакомиться, {message.text}! 🚀\n\n"
        "Сколько тебе лет?"
    )

    await state.set_state(UserState.waiting_for_age)
    @router.message(UserState.waiting_for_age)
async def get_age(message: Message, state: FSMContext):
    await message.answer(
        f"Супер! Тебе {message.text} лет.\n\n"
        "На этом пока всё 😊"
    )

    await state.clear()