from datetime import datetime

def parse_linux_auth(log_text):
    """
    Parses Linux auth.log text and returns a list of events.
    Each event is a dictionary:
        {
            "ts": datetime object,
            "event_type": str,
            "user": str,
            "ip": str
        }
    """
    events = []

    for line in log_text.splitlines():
        # Example: Failed password for root from 10.0.0.5 port 22
        if "Failed password for" in line:
            parts = line.split()
            user_index = parts.index("for") + 1
            ip_index = parts.index("from") + 1
            event = {
                "ts": datetime.now(),  # Placeholder timestamp for now
                "event_type": "ssh_failed",
                "user": parts[user_index],
                "ip": parts[ip_index]
            }
            events.append(event)

    return events
