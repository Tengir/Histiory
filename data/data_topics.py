# Здесь хранятся топики с вопросами.

from data_library.question import Question
from data_library.topic import Topic
from data_library.sub_topic import SubTopic

topics_name = ["Культура СССР", "Правление Романовых", "Древняя Русь"]
sub_topics_name = [["Фильмы", "Плакаты", "Песни", "Архитектура"],
                   ["Персоналии", "События", "Портреты", "Разное"],
                   ["Князья", "Даты", "Термины", "Разное"]]

questions = [[[]], [[]]]


topics = [Topic(topic, f"", [SubTopic(stn, [Question(f"Вопрос{j} {k}", "1", 3) for k in range(4)])
                             for stn in sub_topics_name[i]]) for i, topic in enumerate(topics_name)]
