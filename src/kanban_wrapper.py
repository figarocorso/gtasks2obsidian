class KanbanWrapper:
    def __init__(self, kanban_path, target_section):
        self.kanban_path = kanban_path
        self.target_section = target_section
        self.kanban_lines = self.read_kanban()

    def read_kanban(self):
        with open(self.kanban_path, "r") as kanban_file:
            return kanban_file.readlines()

    def insert_task(self, task_name):
        last_task_index = 0
        in_section = False
        for i, line in enumerate(self.kanban_lines):
            if f"## {self.target_section}" in line:
                in_section = True
                continue

            if not in_section:
                continue

            if "- [ ]" in line:
                last_task_index = i

            if "## " in line:
                break

        if in_section and last_task_index > 0:
            self.kanban_lines.insert(last_task_index + 1, self.task_line(task_name))

    def task_line(self, task_name):
        return f"- [ ] {task_name}\n"

    def write_kanban(self):
        with open(self.kanban_path, "w") as kanban_file:
            for line in self.kanban_lines:
                kanban_file.write(str(line))
