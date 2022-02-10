from aiogram.dispatcher.filters.state import StatesGroup, State


class Game(StatesGroup):
    First = State()
    Second = State()
    Third = State()

