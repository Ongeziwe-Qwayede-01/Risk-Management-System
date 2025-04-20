class Risk:
    def __init__(self, risk_id: str, description: str, severity: str):
        self._risk_id = risk_id
        self._description = description
        self._severity = severity
        self._status = "New"

    def assess(self):
        pass

    def update_status(self, status: str):
        self._status = status

    @property
    def risk_id(self):
        return self._risk_id