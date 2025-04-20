class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = cls.connect()
        return cls._instance

    @staticmethod
    def connect():
        return "Connected to database"

    def get_connection(self):
        return self.connection
