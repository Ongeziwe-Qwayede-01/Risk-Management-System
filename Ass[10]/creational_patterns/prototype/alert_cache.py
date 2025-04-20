from .alert import Alert

class AlertCache:
    def __init__(self):
        self._cache = {}

    def load(self):
        self._cache["critical"] = Alert("high", "System down")
        self._cache["warning"] = Alert("medium", "Disk space low")

    def get_alert(self, key):
        alert = self._cache.get(key)
        return alert.clone() if alert else None