class Topic:
    def __init__(self, name, question_list=[]):
        self.name = name
        self.count_question = len(question_list)
        self.question_list = question_list
