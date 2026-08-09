from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "database/security.db"


def get_events():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM security_events
        ORDER BY id DESC
    """)

    events = cursor.fetchall()

    connection.close()

    return events


@app.route("/")
def dashboard():

    events = get_events()

    total_events = len(events)

    threats = sum(
        1 for event in events
        if event["threat"] == 1
    )

    high_risk = sum(
        1 for event in events
        if event["risk_score"] >= 70
    )

    ai_anomalies = sum(
        1 for event in events
        if event["ai_anomaly"] == 1
    )

    return render_template(
        "index.html",
        events=events,
        total_events=total_events,
        threats=threats,
        high_risk=high_risk,
        ai_anomalies=ai_anomalies
    )


@app.route("/api/events")
def api_events():

    events = get_events()

    data = []

    for event in events:

        data.append({
            "id": event["id"],
            "timestamp": event["timestamp"],
            "event_type": event["event_type"],
            "ip": event["ip"],
            "username": event["username"],
            "severity": event["severity"],
            "message": event["message"],
            "threat": event["threat"],
            "threat_type": event["threat_type"],
            "risk_score": event["risk_score"],
            "ai_anomaly": event["ai_anomaly"]
        })

    return jsonify(data)


@app.route("/api/analytics")
def analytics():

    events = get_events()

    # Severity statistics
    severity = {
        "HIGH": 0,
        "MEDIUM": 0,
        "LOW": 0
    }

    # Threat type statistics
    threat_types = {}

    # Suspicious IP statistics
    suspicious_ips = {}

    # AI anomaly count
    ai_anomalies = 0

    for event in events:

        # -----------------------------
        # Severity Count
        # -----------------------------

        level = event["severity"]

        if level in severity:
            severity[level] += 1


        # -----------------------------
        # Threat Type Count
        # -----------------------------

        threat_type = event["threat_type"]

        if threat_type:
            threat_types[threat_type] = (
                threat_types.get(threat_type, 0) + 1
            )


        # -----------------------------
        # Suspicious IP Count
        # -----------------------------

        if event["threat"] == 1:

            ip = event["ip"]

            suspicious_ips[ip] = (
                suspicious_ips.get(ip, 0) + 1
            )


        # -----------------------------
        # AI Anomaly Count
        # -----------------------------

        if event["ai_anomaly"] == 1:
            ai_anomalies += 1


    # Sort suspicious IPs by number of threats
    suspicious_ips = dict(
        sorted(
            suspicious_ips.items(),
            key=lambda item: item[1],
            reverse=True
        )
    )


    return jsonify({
        "severity": severity,
        "threat_types": threat_types,
        "suspicious_ips": suspicious_ips,
        "ai_anomalies": ai_anomalies
    })


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )