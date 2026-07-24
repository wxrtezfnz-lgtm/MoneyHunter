from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.user_state import UserState
from keyboards.main_keyboard import activity_keyboard
from keyboards.goal_keyboard import goal_keyboard

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
    await state.update_data(name=message.text)

    await message.answer(
        f"Приятно познакомиться, {message.text}! 🚀\n\n"
        "Сколько тебе лет?"
    )

    await state.set_state(UserState.waiting_for_age)


@router.message(UserState.waiting_for_age)
async def get_age(message: Message, state: FSMContext):
    await state.update_data(age=message.text)

    data = await state.get_data()

    await message.answer(
        f"Отлично, {data['name']}! 🎉\n\n"
        "Чем ты сейчас занимаешься?",
        reply_markup=activity_keyboard,
    )

    await state.set_state(UserState.waiting_for_activity)


@router.message(UserState.waiting_for_activity)
async def get_activity(message: Message, state: FSMContext):
    await state.update_data(activity=message.text)

    await message.answer(
        "🎯 Какая у тебя сейчас главная цель?",
        reply_markup=goal_keyboard,
    )

    await state.set_state(UserState.waiting_for_goal)


@router.message(UserState.waiting_for_goal)
async def get_goal(message: Message, state: FSMContext):
    await state.update_data(goal=message.text)

    data = await state.get_data()

    await message.answer(
        "✅ Анкета заполнена!\n\n"
        f"👤 Имя: {data['name']}\n"
        f"🎂 Возраст: {data['age']}\n"
        f"💼 Занятие: {data['activity']}\n"
        f"🎯 Цель: {data['goal']}\n\n"
        "🚀 Скоро я составлю для тебя персональный план заработка!"
    )

    await state.clear()