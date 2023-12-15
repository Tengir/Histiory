from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from utils.send_message import send_message
from utils.generate_keyboard import generate_topic_keyboard

from data.data_topics import topics


router = Router()


@router.callback_query(F.data.startswith('start'))
async def start_quest(callback: CallbackQuery, bot: Bot, state: FSMContext):
    num_topic = int(callback.data.split(":")[1])
    id_msg = callback.message.message_id
    await state.update_data(id_msg=id_msg, num_topic=num_topic)
    msg_ans = topics[num_topic].description
    if msg_ans == "":
        msg_ans = topics[num_topic].name

    id_chat = callback.message.chat.id
    await send_message(id=id_chat, bot=bot, caption=msg_ans, inline_keyboard=generate_topic_keyboard(topics[num_topic]))
    await callback.answer()