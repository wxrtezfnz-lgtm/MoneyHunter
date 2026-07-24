from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.user_state import UserState

from keyboards.main_keyboard import activity_keyboard
from keyboards.goal_keyboard import goal_keyboard
from keyboards.income_keyboard import income_keyboard

from database.db import save_user
from services.advisor import generate_plan

import asyncio

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n\n"
        "Добро пожаловать в Money Hunter AI.\n\n"
        "Напиши, как тебя зовут 😊"
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

    if not message.text.isdigit():
        await message.answer(
            "❌ Возраст должен быть числом.\n\nНапример: 19"
        )
        return

    await state.update_data(age=message.text)

    data = await state.get_data()

    await message.answer(
        f"Отлично, {data['name']}! 🎉\n\n"
        "Чем ты сейчас занимаешься?",
        reply_markup=activity_keyboard
    )

    await state.set_state(UserState.waiting_for_activity)


@router.message(UserState.waiting_for_activity)
async def get_activity(message: Message, state: FSMContext):

    await state.update_data(activity=message.text)

    await message.answer(
        "🎯 Какая у тебя сейчас главная цель?",
        reply_markup=goal_keyboard
    )

    await state.set_state(UserState.waiting_for_goal)


@router.message(UserState.waiting_for_goal)
async def get_goal(message: Message, state: FSMContext):

    await state.update_data(goal=message.text)

    await message.answer(
        "💰 Какой доход ты хочешь получать?",
        reply_markup=income_keyboard
    )

    await state.set_state(UserState.waiting_for_income)


@router.message(UserState.waiting_for_income)
async def get_income(message: Message, state: FSMContext):

    await state.update_data(income=message.text)

    data = await state.get_data()

    save_user(
        telegram_id=message.from_user.id,
        name=data["name"],
        age=data["age"],
        activity=data["activity"],
        goal=data["goal"],
        income=data["income"]
    )

    status = await message.answer("🤖 Анализирую твою анкету...")

    await asyncio.sleep(1)
    await status.edit_text("🧠 Подбираю лучший путь заработка...")

    await asyncio.sleep(1)
    await status.edit_text("📈 Формирую персональный план...")

    await asyncio.sleep(1)

    plan = generate_plan(data)

    await status.edit_text(
        plan,
        parse_mode="HTML"
    )

    await state.clear()