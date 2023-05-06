from models.task.Task import SumTwoNumbers, HelloWorld, QueryChatGpt
from models.queue.Queue import upload_task
import models.queue.Queue


def task_handler(task):
    models.queue.Queue.work_queue.put(task, models.queue.Queue .work_queue)
    return task.uuid


def create_sum_two_numbers(first_num, second_num):
    return task_handler(SumTwoNumbers(first_num, second_num))


def create_hello_world():
    return task_handler(HelloWorld())


def create_query_chat_gpt(prompt):
    return task_handler(QueryChatGpt(prompt))
