from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from data.data_topics import topics

router = Router()


@router.callback_query(F.data.startswith('answer'))
async def get_answer(callback: CallbackQuery, bot: Bot, state: FSMContext):
    print("Зашли в ответы")
    await callback.answer("Ответ записан")
    data: dict = await state.get_data()
    num_topic = data["num_topic"]
    y, x = data["num_question"] # Позиция вопроса.

    first_name = callback.from_user.first_name
    if first_name is None:
        first_name = ""
    last_name = callback.from_user.last_name
    if last_name is None:
        last_name = ""
    username = str(first_name) + " " + str(last_name)

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
