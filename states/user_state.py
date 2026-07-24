from aiogram.fsm.state import State, StatesGroup


class UserState(StatesGroup):
    waiting_for_name = State()
    waiting_for_age = State()
    waiting_for_activity = State()
    waiting_for_goal = State()
    waiting_for_income = State()
    waiting_for_experience = State()