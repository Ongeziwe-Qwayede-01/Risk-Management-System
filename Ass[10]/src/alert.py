class Alert:
    def __init__(self, alert_id: str, message: str, timestamp):
        self._alert_id = alert_id
        self._message = message
        self._timestamp = timestamp

    def notify(self):
        pass