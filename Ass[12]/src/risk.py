import uuid

class Risk:
    def __init__(self, description, severity, likelihood):
        self.id = str(uuid.uuid4())
        self.description = description
        self.severity = severity
        self.likelihood = likelihood
