from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from utils.send_message import send_message
from utils.generate_keyboard import generate_question_keyboard

from data.data_topics import topics
from state import StateBot

router = Router()


@router.callback_query(F.data.startswith('question'), StateFilter(StateBot.passes_quest))
async def question(callback: CallbackQuery, bot: Bot, state: FSMContext):
    data: dict = await state.get_data()
    num_topic = data["num_topic"]

    id_chat = callback.message.chat.id # id чата.

    await bot.delete_message(chat_id=id_chat, message_id=callback.message.message_id) # Удаляем это сообщение.

    x,y = [int(i) for i in callback.data[len("question"):].split(":")]

    question_now = topics[num_topic].sub_topic_list[x].question_list[y]
    msg = question_now.question_text
    await send_message(id_chat, bot, caption=msg, inline_keyboard=generate_question_keyboard(question_now.answer_count))
    await callback.answer()
