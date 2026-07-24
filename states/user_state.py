from aiogram.fsm.state import State, StatesGroup


class UserState(StatesGroup):
    waiting_for_name = State()
    waiting_for_age = State()