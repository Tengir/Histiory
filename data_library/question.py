from data_library.Message import Message


class Question:
    def __init__(self, correct_answer: str, answer_count: int, message_start: Message = None, message_finish: Message = None):
        self.correct_answer = correct_answer
        self.answer_count = answer_count
        self.message_start = message_start
        self.message_finish = message_finish

