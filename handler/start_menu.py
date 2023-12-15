from aiogram import Router, Bot, F
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from utils.send_message import send_message
from utils.generate_keyboard import generate_start_keyboard
from data.data_message import start_message
from state import StateBot

router = Router()


@router.message(F.text.lower().in_(["/start", "запуск", "старт", "начать"]), not StateFilter(StateBot.passes_quest))
async def start_menu(msg: Message, bot: Bot, state: F):
    await send_message(msg.chat.id, bot=bot, caption=start_message, inline_keyboard=generate_start_keyboard())
    await bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id) # Удаляем это сообщение.