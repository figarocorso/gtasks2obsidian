from src.task import Task
from src.tasklist import TaskList


# https://developers.google.com/resources/api-libraries/documentation/tasks/v1/python/latest/tasks_v1.tasks.html
class TasksWrapper:
    def __init__(self, client):
        self.client = client

    def get_uncompleted_tasks(self):
        tasks = []
        for tasklist in self.get_tasklists():
            for task in self.get_uncompleted_tasks_from_tasklist(tasklist):
                tasks.append(task)

        return tasks

    def get_tasklists(self):
        return [TaskList(x)
                for x in self.client.tasklists().list(maxResults=10).execute().get('items', [])]


    def get_uncompleted_tasks_from_tasklist(self, tasklist):
        return [Task(tasklist, x)
                for x in self.client.tasks().list(tasklist=tasklist.id,
                                                  showCompleted=False).execute().get('items', [])]

    def complete_task(self, task):
        target_task = self.get_task(task)
        target_task["status"] = "completed"
        self.client.tasks().patch(tasklist=task.tasklist.id, task=task.id, body=target_task).execute()

    def get_task(self, task):
        return self.client.tasks().get(tasklist=task.tasklist.id, task=task.id).execute()
