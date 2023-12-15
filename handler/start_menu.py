from aiogram import Router, Bot, F
from aiogram.types import Message

from aiogram.fsm.context import FSMContext
from utils.send_message import send_message
from utils.generate_keyboard import generate_start_keyboard
from data.data_message import start_message

router = Router()


@router.message(F.text.lower().in_(["/start", "запуск", "старт", "начать"]))
async def start_menu(msg: Message, bot: Bot, state: F):
    await send_message(msg.chat.id, bot=bot, caption=start_message, inline_keyboard=generate_start_keyboard())