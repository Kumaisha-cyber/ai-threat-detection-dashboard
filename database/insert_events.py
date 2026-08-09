from database.db import get_connection
from utils.log_generator import generate_log
from utils.threat_detector import detect_threat


def insert_event(log, result):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO security_events (
            timestamp,
            event_type,
            ip,
            username,
            severity,
            message,
            threat,
            threat_type,
            risk_score,
            ai_anomaly
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        log["timestamp"],
        log["event_type"],
        log["ip"],
        log["username"],
        log["severity"],
        log["message"],
        int(result["threat"]),
        result["threat_type"],
        result["risk_score"],
        int(result["ai_anomaly"])
    ))

    connection.commit()
    connection.close()


if __name__ == "__main__":

    for _ in range(10):

        log = generate_log()

        result = detect_threat(log)

        insert_event(log, result)

        print(
            f"{log['event_type']} | "
            f"{result['threat_type']} | "
            f"Risk: {result['risk_score']}"
        )
