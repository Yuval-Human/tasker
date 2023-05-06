from queue import Queue
from threading import Thread
from repository.task.store import store
from repository.task.update import update
from models.task.TaskState import TaskState


number_of_threads = 5
work_queue = Queue()


def upload_task(i, q):
    while True:
        task = q.get()
        store({task.uuid: {'state': TaskState.IN_PROGRESS.name}})
        result = task.preform_task()
        update({task.uuid: {'state': TaskState.COMPLETED.name, 'result': result}})


for i in range(number_of_threads):
    worker = Thread(target=upload_task, args=(i, work_queue,))
    worker.setDaemon(True)
    worker.start()

