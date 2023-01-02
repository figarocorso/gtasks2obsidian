from src.google_auth import GoogleAuth
from src.tasks_wrapper import TasksWrapper


def main():
    client = GoogleAuth().tasks_client
    TasksWrapper(client).default_behaviour()


if __name__ == '__main__':
    main()
