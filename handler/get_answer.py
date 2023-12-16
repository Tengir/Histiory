from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from utils.send_message import send_message
from utils.generate_keyboard import generate_question_keyboard

from data.data_topics import topics
from state import StateBot

router = Router()


@router.callback_query(F.data.startswith('answer'), StateFilter(StateBot.passes_quest))
async def get_answer(callback: CallbackQuery, bot: Bot, state: FSMContext):
    print("Зашли в ответы")
    await callback.answer("Ответ записан")
    data: dict = await state.get_data()
    num_topic = data["num_topic"]
    y, x = data["num_question"] # Позиция вопроса.
    username = str(callback.from_user.first_name) + " " + str(callback.from_user.last_name)

    id_chat = callback.message.chat.id # id чата.

    ans_user = int(callback.data[len("answer"):])
    question_now = topics[num_topic].sub_topic_list[x].question_list[y]

    # Записываем ответ пользователя.
    answers_now_question = data["answers_now_question"]
    answers_now_question[username] = str(ans_user + 1)

    # # Прибавляем, если правильно ответил.
    # score_users = data["score_users"]
    # score_users[username] = score_users.setdefault(username, 0)
    # if str(ans_user + 1) == question_now.correct_answer:
    #     score_users[username] += 1
    await state.update_data(answers_now_question=answers_now_question)
