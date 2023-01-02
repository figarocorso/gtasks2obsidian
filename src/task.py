class Task:

    def __init__(self, tasklist, raw_task):
        self.tasklist = tasklist
        self.id = raw_task["id"]
        self.name = raw_task["title"]
        self.body = raw_task

    def __str__(self):
        return f"{self.tasklist.name}/{self.name}"
