def detect_threat(log):
    event_type = log.get("event_type")
    severity = log.get("severity")

    threat = False
    threat_type = "Normal Activity"
    risk_score = 0

    if event_type == "PORT_SCAN":
        threat = True
        threat_type = "Port Scan"
        risk_score = 85

    elif event_type == "SUSPICIOUS_LOGIN":
        threat = True
        threat_type = "Suspicious Login"
        risk_score = 80

    elif event_type == "LOGIN_FAILED":
        threat = True
        threat_type = "Failed Login Attempt"
        risk_score = 50

    elif severity == "HIGH":
        threat = True
        threat_type = "High Severity Activity"
        risk_score = 75

    return {
        "threat": threat,
        "threat_type": threat_type,
        "risk_score": risk_score,
        "severity": severity
    }


if __name__ == "__main__":
    sample_log = {
        "event_type": "PORT_SCAN",
        "severity": "HIGH"
    }

    result = detect_threat(sample_log)

    print("Threat Detection Result:")
    print(result)
