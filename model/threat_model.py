from model.threat_model import train_model
import numpy as np


ai_model = train_model()


def detect_threat(log):

    event_type = log.get("event_type")
    severity = log.get("severity")

    # Rule-based detection
    threat = False
    threat_type = "Normal Activity"
    risk_score = 10

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

    # Convert log into ML features
    event_mapping = {
        "LOGIN_SUCCESS": 1,
        "LOGIN_FAILED": 2,
        "PORT_SCAN": 3,
        "SUSPICIOUS_LOGIN": 4,
        "FILE_ACCESS": 5
    }

    severity_mapping = {
        "LOW": 1,
        "MEDIUM": 2,
        "HIGH": 3
    }

    event_value = event_mapping.get(event_type, 0)
    severity_value = severity_mapping.get(severity, 0)

    features = np.array([
        [event_value, severity_value, risk_score]
    ])

    prediction = ai_model.predict(features)[0]

    ai_anomaly = prediction == -1

    # Combine rule detection + AI detection
    if ai_anomaly:
        threat = True

        if threat_type == "Normal Activity":
            threat_type = "AI Detected Anomaly"

        risk_score = max(risk_score, 70)

    return {
        "threat": threat,
        "threat_type": threat_type,
        "risk_score": risk_score,
        "severity": severity,
        "ai_anomaly": ai_anomaly
    }


if __name__ == "__main__":

    sample_log = {
        "event_type": "PORT_SCAN",
        "severity": "HIGH"
    }

    result = detect_threat(sample_log)

    print("AI Threat Detection Result:")
    print(result)