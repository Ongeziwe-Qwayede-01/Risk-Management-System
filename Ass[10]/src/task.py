class Task:
    def __init__(self, task_id: str, description: str):
        self._task_id = task_id
        self._description = description
        self._completed = False

    def complete(self):
        self._completed = True