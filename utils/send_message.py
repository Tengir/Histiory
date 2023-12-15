import logging

from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.types.input_media_video import InputMediaVideo
from aiogram.types.input_file import FSInputFile
from aiogram.types import InlineKeyboardMarkup


async def send_message(id: int, bot: Bot, caption: str="", video: str=None, photo: str=None, audio: str=None, inline_keyboard: InlineKeyboardMarkup=None):
    if video is not None:
        await bot.send_video(id, video=video,
                             caption=caption, reply_markup=inline_keyboard)
        return

    if audio is not None:
        await bot.send_voice(id, voice=audio,
                             caption=caption, reply_markup=inline_keyboard)
        return

    if photo is not None:
        await bot.send_photo(id, photo=photo,
                             caption=caption, reply_markup=inline_keyboard)
        return

    await bot.send_message(id, text=caption, reply_markup=inline_keyboard)