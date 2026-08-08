import random
from datetime import datetime


IP_ADDRESSES = [
    "192.168.1.10",
    "192.168.1.15",
    "10.0.0.25",
    "172.16.0.8",
    "203.0.113.45"
]

USERS = [
    "admin",
    "user1",
    "user2",
    "guest",
    "developer"
]

EVENT_TYPES = [
    "LOGIN_SUCCESS",
    "LOGIN_FAILED",
    "PORT_SCAN",
    "SUSPICIOUS_LOGIN",
    "FILE_ACCESS"
]


def generate_log():
    event_type = random.choice(EVENT_TYPES)
    ip = random.choice(IP_ADDRESSES)
    username = random.choice(USERS)

    if event_type == "LOGIN_SUCCESS":
        severity = "LOW"
        message = f"Successful login by {username}"

    elif event_type == "LOGIN_FAILED":
        severity = "MEDIUM"
        message = f"Failed login attempt by {username}"

    elif event_type == "PORT_SCAN":
        severity = "HIGH"
        message = f"Port scanning activity detected from {ip}"

    elif event_type == "SUSPICIOUS_LOGIN":
        severity = "HIGH"
        message = f"Suspicious login detected for {username}"

    else:
        severity = "LOW"
        message = f"File accessed by {username}"

    log = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "event_type": event_type,
        "ip": ip,
        "username": username,
        "severity": severity,
        "message": message
    }

    return log


if __name__ == "__main__":
    for _ in range(10):
        print(generate_log())
