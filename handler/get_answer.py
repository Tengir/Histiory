from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from utils.send_message import send_message
from utils.generate_keyboard import generate_question_keyboard

from data.data_topics import topics
from state import StateBot

router = Router()


@router.callback_query(F.data.startswith('answer'), StateFilter(StateBot.passes_quest))
async def get_answer(callback: CallbackQuery, bot: Bot, state: FSMContext):
    data: dict = await state.get_data()
    num_topic = data["num_topic"]
    y, x = data["num_question"] # Позиция вопроса.

    id_chat = callback.message.chat.id # id чата.

    ans = int(callback.data[len("answer"):])
    question_now = topics[num_topic].sub_topic_list[x].question_list[y]
    msg = question_now.message_start.information
    await send_message(id_chat, bot, caption=msg, inline_keyboard=generate_question_keyboard(question_now.answer_count))
    await callback.answer()
