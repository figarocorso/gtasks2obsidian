from src.google_auth import GoogleAuth
from src.tasks_wrapper import TasksWrapper


def main():
    uncompleted_tasks = TasksWrapper(GoogleAuth().tasks_client).get_uncompleted_tasks()
    for task in uncompleted_tasks:
        print(task)


if __name__ == '__main__':
    main()
