class MitigationPlan:
    def __init__(self):
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)

    def show_plan(self):
        return " -> ".join(self.steps)