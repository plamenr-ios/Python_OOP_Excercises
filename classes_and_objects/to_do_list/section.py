from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if not new_task in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        for i in self.tasks:
            if task_name in i.details():
                i.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        amount = 0
        for i in self.tasks:
            if i.completed:
                self.tasks.remove(i)
                amount += 1
        return f"Cleared {amount} tasks."

    def view_section(self):
        str = ""
        str += f"Section {self.name}:"
        for i in self.tasks:
            str += '\n' + i.details()
        return str


