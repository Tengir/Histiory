from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
import asyncio

from utils.send_message import send_message
from utils.generate_keyboard import generate_question_keyboard, generate_topic_keyboard
from utils.generate_top import generate_top

from data.data_topics import topics
from state import StateBot

router = Router()


@router.callback_query(F.data.startswith('question'), StateFilter(StateBot.passes_quest))
async def question(callback: CallbackQuery, bot: Bot, state: FSMContext):
    print("Зашли в квестион")
    data: dict = await state.get_data()
    num_topic = data["num_topic"]
    id_chat = callback.message.chat.id # id чата.

    y,x = [int(i) for i in callback.data[len("question"):].split(":")] # Расположение вопроса в таблице.
    if (y, x) in data["used_question"]:
        await callback.answer("Нельзя выбрать")
        return
    await state.update_data(num_question=(x, y))

    await bot.delete_message(chat_id=id_chat,
                             message_id=callback.message.message_id)  # Удаляем это сообщение.

    question_now = topics[num_topic].sub_topic_list[x].question_list[y]
    msg_send = question_now.message_start
    print("Отправляем вопрос")

    msg_question = await send_message(id_chat, bot,caption=f"Осталось 15\n", message=msg_send, inline_keyboard=generate_question_keyboard(question_now.answer_count))
    await state.update_data(bot_quest_message=msg_question.message_id)
    print(msg_question)
    ###########################################################################

    # Меняем оставшееся время в сообщении.
    print("Зашли в таймер")
    for i in range(1, 5):
        print("ждем")
        await asyncio.sleep(3)  # ИГРОКИ ОТВЕЧАЮТ.
        # Сообщения с медиа имеют caption и меняются по-разному.
        print("подождали")
        if msg_question.caption is not None:
            await bot.edit_message_caption(chat_id=id_chat, message_id=msg_question.message_id,
                                           caption=f"Осталось {15-i * 3}\n" + question_now.message_start.information,
                                           reply_markup=generate_question_keyboard(question_now.answer_count))
        else:
            await bot.edit_message_text(chat_id=id_chat, message_id=msg_question.message_id,
                                        text=f"Осталось {15-i * 3}\n" + question_now.message_start.information
                                        , reply_markup=generate_question_keyboard(question_now.answer_count))
    print("Вышли таймер")
    ###########################################################################

    # Удаляем сообщение с выбором ответа на вопрос.

    await bot.delete_message(chat_id=id_chat,
                             message_id=msg_question.message_id)  # Удаляем сообщение с вопросом.
    used_question = data["used_question"]
    used_question.add((y, x))
    await state.update_data(used_question=used_question)

    ###########################################################################

    # Игроки смотрят ответ.
    print("Зашли смотреть ответ")
    msg_send = question_now.message_finish
    msg_question = await send_message(id_chat, bot, message=msg_send)
    await state.update_data(bot_quest_message=msg_question.message_id)
    await asyncio.sleep(8)
    await bot.delete_message(chat_id=id_chat,
                             message_id=msg_question.message_id)  # Удаляем сообщение с ответом.
    print("Вышли смотреть ответ")

    ###########################################################################

    print("Работает с ответами")
    # Проверяем записанные ответы пользователей.

    data: dict = await state.get_data() # Наша дата обновилась после ответов.
    score_users = data["score_users"]
    for username in data["answers_now_question"].keys():
        ans_user = data["answers_now_question"][username] # Записанный ответ пользователя.
        score_users[username] = score_users.setdefault(username, 0)
        if ans_user == question_now.correct_answer: # Прибавляем, если правильно ответил.
            score_users[username] += 1
    await state.update_data(score_users=score_users)
    print("Закончили с ответами")
    ###########################################################################

    # Выслыаем таблицу с вопросами.
    msg_ans = topics[num_topic].description
    if msg_ans == "":
        msg_ans = topics[num_topic].name

    score_users = data["score_users"]
    print("Готовимя высылать таблицу воппросов")
    print(used_question)
    print(generate_top(score_users)+msg_ans)
    msg = await send_message(id=id_chat, bot=bot,
                       caption=generate_top(score_users)+msg_ans,
                       inline_keyboard=generate_topic_keyboard(topics[num_topic], used_question))

    await state.update_data(bot_quest_message=msg.message_id)
    print("Выслали таблицу")



