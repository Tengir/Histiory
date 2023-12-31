from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from utils.send_message import send_message
from utils.generate_keyboard import generate_topic_keyboard

from data.data_topics import topics


router = Router()


@router.callback_query(F.data.startswith('start'))
async def start_quest(callback: CallbackQuery, bot: Bot, state: FSMContext):
    data: dict = await state.get_data()
    id_chat = callback.message.chat.id  # id чата.
    await bot.delete_message(chat_id=id_chat, message_id=callback.message.message_id) # Удаляем предыдущ. сообщ..
    # Удаляем прошлый квест, который был начат.
    if "bot_quest_message" in data.keys() and data["bot_quest_message"] != "":
        await bot.delete_message(chat_id=id_chat,
                                 message_id=data["bot_quest_message"])

    num_topic = int(callback.data.split(":")[1])

    msg_ans = topics[num_topic].description
    if msg_ans == "":
        msg_ans = topics[num_topic].name

    msg = await send_message(id=id_chat, bot=bot, caption=msg_ans, inline_keyboard=generate_topic_keyboard(topics[num_topic]))
    await state.clear()
    await state.update_data(num_topic=num_topic, score_users=dict(),
                            used_question=set(), answers_now_question=dict(),
                            bot_quest_message=msg.message_id)
    await callback.answer()