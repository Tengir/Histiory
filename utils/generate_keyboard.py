from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.data_topics import topics
from data_library.topic import Topic



def generate_question_keyboard(num: int):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=str(i), callback_data=str(i - 1))] for i in
        range(1, num + 1)
    ], resize_keyboard=True)
    return kb


def generate_topic_keyboard(topic:Topic):
    names = [sub_top.name for sub_top in topic.sub_topic_list]
    row = topic.len_sub_topic
    col = topic.count_sub_topic
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=names[i], callback_data="") for i in
         range(col)],
        *[[InlineKeyboardButton(text=str(i + 1), callback_data=str(i - 1)) for i
          in range(col)] for j in range(row)]
    ], resize_keyboard=True)
    return kb


def generate_start_keyboard():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=topics[i].name, callback_data=f"start:{i}")]
        for i
        in range(len(topics))
    ], resize_keyboard=True)
    return kb
