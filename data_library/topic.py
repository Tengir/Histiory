from data_library.sub_topic import SubTopic


class Topic:
    def __init__(self, name, description: str = "", sub_topic_list: list = None):
        self.name = name
        self.description = description
        self.count_sub_topic = len(sub_topic_list)
        self.len_sub_topic = len(sub_topic_list[0].question_list)
        self.sub_topic_list = sub_topic_list
