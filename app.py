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
        1
        for event in events
        if event["threat"] == 1
    )

    high_risk = sum(
        1
        for event in events
        if event["risk_score"] >= 70
    )

    ai_anomalies = sum(
        1
        for event in events
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

@app.route("/health")
def health():
    return jsonify({
        "status": "online",
        "service": "AI Threat Detection Dashboard"
    })

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



if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
