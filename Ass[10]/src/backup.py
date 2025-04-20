class Backup:
    def __init__(self, backup_id: str, schedule: str):
        self._backup_id = backup_id
        self._schedule = schedule

    def perform_backup(self):
        pass