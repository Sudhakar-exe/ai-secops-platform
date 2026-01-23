from collections import defaultdict

THRESHOLD = 2  # failed attempts

def detect_ssh_bruteforce(events):
    """
    Detect SSH brute-force attacks from parsed events
    """
    failed_by_ip = defaultdict(int)
    alerts = []

    for event in events:
        if event["event_type"] == "ssh_failed":
            failed_by_ip[event["ip"]] += 1

    for ip, count in failed_by_ip.items():
        if count >= THRESHOLD:
            alerts.append({
                "alert_type": "SSH Brute Force",
                "ip": ip,
                "attempts": count,
                "severity": "HIGH"
            })

    return alerts
