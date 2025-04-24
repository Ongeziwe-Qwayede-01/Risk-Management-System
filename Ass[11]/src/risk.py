class Risk:
    def __init__(self, risk_id, description, severity, likelihood):
        self.risk_id = risk_id
        self.description = description
        self.severity = severity
        self.likelihood = likelihood

    def __repr__(self):
        return f"Risk({self.risk_id}, {self.description}, {self.severity}, {self.likelihood})"
