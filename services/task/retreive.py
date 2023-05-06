from repository.task.retrieve import get
from models.task.TaskState import TaskState


def retrieve(uuid):
    task = get(uuid)
    if task is None:
        return {'res': 'No such task :('}

    elif task['state'] == str(TaskState.IN_PROGRESS.name):
        return {'res': 'Task is currently in progress'}

    else:
        return {'res': task['result']}

