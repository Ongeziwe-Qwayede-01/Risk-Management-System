from creational_patterns.singleton.database_connection import DatabaseConnection

def test_singleton_connection():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    assert db1 is db2
    assert db1.get_connection() == "Connected to database"
