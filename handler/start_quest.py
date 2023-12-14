from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from utils.send_message import send_message
from utils.generate_keyboard import generate_start_keyboard
from data.data_message import start_message


router = Router()


@router.callback_query(F.data.startswith == 'start')
async def start_quest(callback: CallbackQuery, bot: Bot, state: FSMContext):
    num_topic = int(CallbackQuery.data.split(":")[1])
    id_msg = callback.message.message_id
    state
    await send_message(msg.from_user.id, bot=bot, caption=start_message, inline_keyboard=generate_start_keyboard())