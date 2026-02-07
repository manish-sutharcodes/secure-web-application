document.addEventListener("DOMContentLoaded", () => {
    const logs = document.querySelector(".soc-logs");
    if (!logs) return;

    const fakeEvents = [
        "[INFO] Session heartbeat OK",
        "[INFO] Admin activity logged",
        "[WARNING] Multiple requests detected from IP 192.168.1.23",
        "[WARNING] Suspicious behavior from IP 10.0.0.45",
        "[CRITICAL] Brute-force attempt blocked from IP 185.203.112.7",
        "[CRITICAL] Malicious IP blacklisted: 203.0.113.99",
        "[INFO] Firewall rules updated"
    ];

    setInterval(() => {
        const li = document.createElement("li");
        const text = fakeEvents[Math.floor(Math.random() * fakeEvents.length)];
        li.innerText = text;

        if (text.includes("CRITICAL")) li.className = "critical";
        else if (text.includes("WARNING")) li.className = "warning";
        else li.className = "info";

        logs.prepend(li);

        if (logs.children.length > 6) {
            logs.removeChild(logs.lastChild);
        }
    }, 4000);
});
