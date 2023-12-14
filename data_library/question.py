class Question:
    def __init__(self, question_text, correct_answer: str, answer_count: int, video=None, audio=None):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.answer_count = answer_count
        self.video = video
        self.audio = audio
