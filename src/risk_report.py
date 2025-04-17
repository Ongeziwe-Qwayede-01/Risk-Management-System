class RiskReport:
    def __init__(self, report_id: str):
        self._report_id = report_id
        self._entries = []

    def add_entry(self, entry):
        self._entries.append(entry)

    def generate(self):
        pass