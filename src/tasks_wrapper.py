# https://developers.google.com/resources/api-libraries/documentation/tasks/v1/python/latest/tasks_v1.tasks.html


class TasksWrapper:
    def __init__(self, client):
        self.client = client

    def default_behaviour(self):
        results = self.client.tasklists().list(maxResults=10).execute()
        tasklists = results.get('items', [])

        if not tasklists:
            print('No task lists found.')
            return

        for tasklist in tasklists:
            print(f"{tasklist['title']} - {tasklist['id']}")
            # for task in self.client.tasks().list(tasklist=tasklist['id']).execute().get('items', []):
            for task in self.client.tasks().list(tasklist=tasklist['id'], showCompleted=False).execute().get('items', []):
                print(f"  {task.get('title', '')} - {task['id']}")

        # task = self.client.tasks().get(tasklist="dURER2x6QzRMUUtCcDRldw", task="ejBzcGxFR0ZPalQ2ako3SA").execute()
        # task["status"] = "completed"
        # self.client.tasks().patch(tasklist="dURER2x6QzRMUUtCcDRldw", task="ejBzcGxFR0ZPalQ2ako3SA", body=task).execute()
        print(self.client.tasks().get(tasklist="dURER2x6QzRMUUtCcDRldw", task="ejBzcGxFR0ZPalQ2ako3SA").execute())
