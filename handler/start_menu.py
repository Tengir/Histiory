from aiogram import Router, Bot, F
from aiogram.types import Message

from utils.send_message import send_message
from utils.generate_keyboard import generate_start_keyboard
from data.data_message import start_message

router = Router()


@router.message(F.text.lower().in_(["/start", "запуск", "старт", "начать"]))
async def start_menu(msg: Message, bot: Bot):
    await send_message(msg.from_user.id, bot=bot, caption=start_message, inline_keyboard=generate_start_keyboard())