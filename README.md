# 🛡️ AI Threat Detection Dashboard

### Real-Time Security Monitoring & AI Anomaly Detection

A web-based cybersecurity dashboard built with **Python Flask, SQLite, JavaScript, HTML, CSS and Scikit-learn** for monitoring security events, identifying threats, calculating risk scores and detecting suspicious anomalies.

---

## 🚀 Project Overview

The **AI Threat Detection Dashboard** is designed to provide a simple Security Operations Center (SOC)-style monitoring interface.

The application collects security events from a SQLite database and displays them in a real-time dashboard.

It provides security analysts with information such as:

- Total security events
- Detected threats
- High-risk events
- AI-detected anomalies
- Event severity
- Threat type
- IP address
- Username
- Risk score
- Event timestamp

---

## ✨ Features

### 📊 Security Dashboard

Displays important security statistics:

- **Total Events**
- **Threats Detected**
- **High Risk Events**
- **AI Anomalies**

---

### 🚨 Threat Detection

The system identifies different types of security events including:

- `LOGIN_SUCCESS`
- `LOGIN_FAILED`
- `PORT_SCAN`
- `SUSPICIOUS_LOGIN`
- `FILE_ACCESS`

---

### 🤖 AI Anomaly Detection

Security events can be marked as AI anomalies.

Example:

```text
🤖 DETECTED

📈 Risk Score

Each security event contains a risk score.

Example:

Risk Score	Level
10	Low
50	Medium
70+	High
80+	Critical/Suspicious
🔎 Search

Security events can be searched using:

Event type
IP address
Username
Threat type
🎯 Severity Filter

Events can be filtered by:

All
High
Medium
Low
🔄 Real-Time Updates

The dashboard automatically requests updated security events from the Flask API every 5 seconds.

Users can also manually refresh the dashboard.

🧰 Technologies Used
Backend
Python
Flask
SQLite
Frontend
HTML5
CSS3
JavaScript
AI / Machine Learning
Scikit-learn
Development Tools
Git
GitHub
GitHub Codespaces
VS Code
📂 Project Structure
ai-threat-detection-dashboard/
│
├── app.py
│
├── database/
│   ├── security.db
│   └── insert_events.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
├── README.md
└── requirements.txt
⚙️ Installation
1. Clone the repository
git clone https://github.com/Kumaisha-cyber/ai-threat-detection-dashboard.git
2. Enter the project directory
cd ai-threat-detection-dashboard
3. Install dependencies
pip install -r requirements.txt
▶️ Run the Application

Start the Flask application:

python app.py

The application will run on:

http://127.0.0.1:5000

Open the address in your browser.

🔌 REST API

The project provides an API endpoint for security events:

GET /api/events

Example:

curl http://127.0.0.1:5000/api/events

The API returns event information such as:

ID
Timestamp
Event Type
IP Address
Username
Severity
Threat Type
Risk Score
AI Anomaly
🗄️ Database

The project uses SQLite to store security events.

Database:

database/security.db

Security events are retrieved from the:

security_events

table.

🛡️ Example Security Events
Suspicious Login
Event Type: SUSPICIOUS_LOGIN
Threat Type: Suspicious Login
Risk Score: 80
AI: DETECTED
Port Scan
Event Type: PORT_SCAN
Threat Type: Port Scan
Risk Score: 85
Failed Login
Event Type: LOGIN_FAILED
Threat Type: Failed Login Attempt
Risk Score: 50
File Access Anomaly
Event Type: FILE_ACCESS
Threat Type: AI Detected Anomaly
Risk Score: 70
AI: DETECTED
🔄 Real-Time Monitoring Flow
Security Events
       ↓
SQLite Database
       ↓
Flask Backend
       ↓
REST API
       ↓
JavaScript
       ↓
Dashboard
       ↓
Threat & AI Monitoring
📊 Dashboard Information

The dashboard provides a centralized view of security activity.

Example metrics:

Total Events       → 40
Threats Detected   → 35
High Risk          → 29
AI Anomalies       → 21

These values are calculated from the security events stored in the database.

🎯 Project Goals

The main goals of this project are:

Build a security monitoring dashboard
Monitor security events
Identify suspicious activities
Display risk scores
Detect AI-based anomalies
Provide real-time event updates
Practice Python Flask development
Practice cybersecurity concepts
Build a practical cybersecurity portfolio project
🔮 Future Improvements

Possible future improvements include:

📧 Email security alerts
🔔 Real-time notifications
📊 Security charts and graphs
🌍 IP geolocation
👤 User authentication
🔐 Role-based access control
📋 Export security reports
🤖 Advanced machine-learning models
🧠 Improved anomaly detection
☁️ Cloud deployment
📱 Improved mobile dashboard
🔐 Disclaimer

This project is created for educational and cybersecurity learning purposes.

The security events used in this project are simulated test data.

👩‍💻 Author
Kumaisha-cyber

Python Developer | Cybersecurity Enthusiast

GitHub:

https://github.com/Kumaisha-cyber