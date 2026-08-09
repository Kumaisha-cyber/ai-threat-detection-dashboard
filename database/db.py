import sqlite3
import os


DATABASE_PATH = "database/security.db"


def get_connection():
    os.makedirs("database", exist_ok=True)
    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS security_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            event_type TEXT,
            ip TEXT,
            username TEXT,
            severity TEXT,
            message TEXT,
            threat INTEGER,
            threat_type TEXT,
            risk_score INTEGER,
            ai_anomaly INTEGER
        )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    initialize_database()
    print("Security database initialized successfully.")