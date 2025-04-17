class User:
    def __init__(self, user_id: str, name: str):
        self._user_id = user_id
        self._name = name

    def borrow_risk(self, risk):
        pass  # Placeholder for logic

    def return_risk(self, risk):
        pass

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name