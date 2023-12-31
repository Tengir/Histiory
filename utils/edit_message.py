from aiogram import Bot

from aiogram.types import InlineKeyboardMarkup

from data_library.message import Message


async def send_message(id: int, id_msg: int, bot: Bot, caption: str="", video: str=None, photo: str=None, voice: str=None, inline_keyboard: InlineKeyboardMarkup=None, message: Message=None):


    if message is not None:
        caption=message.information
        video=message.video
        photo=message.photo
        voice = message.audio
    if video is not None:
        msg = await bot.send_video(id, video=video,
                             caption=caption, reply_markup=inline_keyboard)

    elif voice is not None:
        msg = await bot.send_voice(id, voice=voice,
                             caption=caption, reply_markup=inline_keyboard)

    elif photo is not None:
        msg = await bot.send_photo(id, photo=photo,
                             caption=caption, reply_markup=inline_keyboard)
    else:
        msg = await bot.send_message(id, text=caption, reply_markup=inline_keyboard)

    return msg