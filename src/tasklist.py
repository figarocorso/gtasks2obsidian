class TaskList:

    def __init__(self, raw_tasklist):
        self.id = raw_tasklist["id"]
        self.name = raw_tasklist["title"]
        self.body = raw_tasklist

    def __str__(self):
        return f"{self.name}"
