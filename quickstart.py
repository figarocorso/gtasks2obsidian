from src.google_auth import GoogleAuth
from src.tasks_wrapper import TasksWrapper
from src.kanban_wrapper import KanbanWrapper

import json


CONFIG_FILE = "config.json"

def main():
    config = load_config()
    kanban = KanbanWrapper(config["kanban_path"], config["target_list"])
    tasks_wrapper = TasksWrapper(GoogleAuth().tasks_client)
    uncompleted_tasks = tasks_wrapper.get_uncompleted_tasks()
    for task in uncompleted_tasks:
        print(task)
        kanban.insert_task(task.name)
        tasks_wrapper.complete_task(task)

    kanban.write_kanban()


def load_config():
    with open(CONFIG_FILE) as config_file:
        config = json.load(config_file)
    return config


if __name__ == '__main__':
    main()
