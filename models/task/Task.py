from abc import ABC, abstractmethod
import uuid
import time
from controllers.chatGpt.chatGpt import query


class Task(ABC):
    def __init__(self):
        self.uuid = str(uuid.uuid4())

    @abstractmethod
    def preform_task(self):
        pass


class SumTwoNumbers(Task):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def preform_task(self):
        return str(self.x+self.y)


class HelloWorld(Task):
    def __init__(self):
        super().__init__()

    def preform_task(self):
        time.sleep(100)
        return 'Hello World!'


class QueryChatGpt(Task):
    def __init__(self, prompt):
        super().__init__()
        self.prompt = prompt

    def preform_task(self):
        return query(self.prompt)
