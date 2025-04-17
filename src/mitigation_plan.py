class MitigationPlan:
    def __init__(self, plan_id: str):
        self._plan_id = plan_id
        self._tasks = []

    def add_task(self, task):
        self._tasks.append(task)

    def get_tasks(self):
        return self._tasks