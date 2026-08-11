let allEvents = [];


// ================================
// LOAD EVENTS FROM API
// ================================

async function loadEvents() {

    try {

        const response = await fetch("/api/events");

        if (!response.ok) {
            throw new Error("API request failed");
        }

        allEvents = await response.json();

        updateStatistics();
        renderEvents();

        document.getElementById("lastUpdated").textContent =
            "Updated: " + new Date().toLocaleTimeString();

    } catch (error) {

        console.error("Error loading events:", error);

        document.getElementById("lastUpdated").textContent =
            "Update failed";

    }

}


// ================================
// UPDATE STATISTICS
// ================================

function updateStatistics() {

    const total = allEvents.length;

    const threats = allEvents.filter(
        event => Number(event.threat) === 1
    ).length;

    const highRisk = allEvents.filter(
        event => Number(event.risk_score) >= 70
    ).length;

    const aiAnomalies = allEvents.filter(
        event => Number(event.ai_anomaly) === 1
    ).length;


    document.getElementById("totalEvents").textContent = total;

    document.getElementById("threats").textContent = threats;

    document.getElementById("highRisk").textContent = highRisk;

    document.getElementById("aiAnomalies").textContent = aiAnomalies;

}


// ================================
// RENDER EVENTS
// ================================

function renderEvents() {

    const table = document.getElementById("eventsTable");

    const searchValue =
        document
            .getElementById("searchInput")
            .value
            .toLowerCase();

    const severity =
        document
            .getElementById("severityFilter")
            .value;


    table.innerHTML = "";


    const filteredEvents = allEvents.filter(event => {

        const searchText = (

            event.event_type +
            " " +
            event.ip +
            " " +
            event.username +
            " " +
            event.threat_type

        ).toLowerCase();


        const matchesSearch =
            searchText.includes(searchValue);


        const matchesSeverity =
            severity === "ALL" ||
            event.severity === severity;


        return matchesSearch && matchesSeverity;

    });


    filteredEvents.forEach(event => {

        const row = document.createElement("tr");


        // Severity badge

        let severityClass = "low";

        if (event.severity === "HIGH") {
            severityClass = "high";
        }

        else if (event.severity === "MEDIUM") {
            severityClass = "medium";
        }


        // AI status

        let aiStatus;

        if (Number(event.ai_anomaly) === 1) {

            aiStatus =
                `<span class="ai-detected">
                    🤖 DETECTED
                 </span>`;

        } else {

            aiStatus =
                `<span class="normal">
                    NORMAL
                 </span>`;

        }


        // Risk class

        let riskClass = "risk-low";

        if (Number(event.risk_score) >= 70) {

            riskClass = "risk-high";

        }

        else if (Number(event.risk_score) >= 50) {

            riskClass = "risk-medium";

        }


        row.innerHTML = `

            <td>
                ${event.timestamp}
            </td>

            <td>
                <span class="event-type">
                    ${event.event_type}
                </span>
            </td>

            <td>
                ${event.ip}
            </td>

            <td>
                ${event.username}
            </td>

            <td>
                <span class="badge ${severityClass}">
                    ${event.severity}
                </span>
            </td>

            <td>
                ${event.threat_type}
            </td>

            <td>
                <span class="risk-score ${riskClass}">
                    ${event.risk_score}
                </span>
            </td>

            <td>
                ${aiStatus}
            </td>

        `;


        table.appendChild(row);

    });


    if (filteredEvents.length === 0) {

        table.innerHTML = `

            <tr>

                <td colspan="8" class="no-events">

                    🔍 No matching security events found

                </td>

            </tr>

        `;

    }

}


// ================================
// SEARCH
// ================================

document
    .getElementById("searchInput")
    .addEventListener(
        "input",
        renderEvents
    );


// ================================
// SEVERITY FILTER
// ================================

document
    .getElementById("severityFilter")
    .addEventListener(
        "change",
        renderEvents
    );


// ================================
// REFRESH BUTTON
// ================================

document
    .getElementById("refreshButton")
    .addEventListener(
        "click",
        loadEvents
    );


// ================================
// AUTO REFRESH
// ================================

// Update dashboard every 5 seconds

setInterval(
    loadEvents,
    5000
);


// ================================
// INITIAL LOAD
// ================================

loadEvents();