from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.data_topics import topics


def generate_question_keyboard(num: int):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=str(i), callback_data=str(i - 1))] for i in
        range(1, num + 1)
    ], resize_keyboard=True)
    return kb


def generate_start_keyboard():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=topics[i].name, callback_data=f"start:{i}")] for i
        in range(len(topics))
    ], resize_keyboard=True)
    return kb
