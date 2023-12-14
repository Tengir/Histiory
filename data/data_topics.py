# Здесь хранятся топики с вопросами.

from data_library.question import Question
from data_library.topic import Topic
from data_library.sub_topic import SubTopic

topics = [Topic(f"Топик{i}", f"Описание топика{i}", [SubTopic(f"СапТопик{j}", [Question(f"Вопрос{j} {k}", "1", 3) for k in range(4)]) for j in range(4)]) for i in range(4)]