import copy

class Alert:
    def __init__(self, severity, message):
        self.severity = severity
        self.message = message

    def clone(self):
        return copy.deepcopy(self)