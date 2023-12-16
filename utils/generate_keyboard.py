from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.data_topics import topics
from data_library.topic import Topic


def generate_final_keyboard(num: int):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Запустить ещё раз",
                              callback_data=f"restart")]
    ], resize_keyboard=True)
    return kb


def generate_question_keyboard(num: int):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f"{i + 1}", callback_data=f"answer{i}")] for
        i in
        range(num)
    ], resize_keyboard=True)
    return kb


def generate_topic_keyboard(topic: Topic, used_buttons: set = None):
    used_buttons = set() if used_buttons is None else used_buttons
    names = [sub_top.name for sub_top in topic.sub_topic_list]
    row = topic.len_sub_topic
    col = topic.count_sub_topic
    kb = InlineKeyboardMarkup(inline_keyboard=
                              [[InlineKeyboardButton(text=names[i],
                                                     callback_data="None") for
                                i in range(col)]] +
                              [[InlineKeyboardButton(text=str((j + 1) * 10),
                                                     callback_data=f"question{j}:{i}") if (
                                                                                          j,
                                                                                          i) not in used_buttons
                                else InlineKeyboardButton(text="❌",
                                                          callback_data="None")
                                for i in
                                range(col)] for j in range(row)],
                              resize_keyboard=True)
    return kb


def generate_start_keyboard():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=topics[i].name, callback_data=f"start:{i}")]
        for i
        in range(len(topics))
    ], resize_keyboard=True)
    return kb
