from aiogram.fsm.state import State, StatesGroup


class StateBot(StatesGroup):
    passes_quest = State()