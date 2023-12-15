from data_library.question import Question


class SubTopic:
    def __init__(self, name, question_list: list = None):
        self.name = name
        self.question_list = question_list
