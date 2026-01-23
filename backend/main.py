from fastapi import FastAPI
from app.parsers.linux_auth import parse_linux_auth
from app.detectors.ssh_bruteforce import detect_ssh_bruteforce
from pydantic import BaseModel

app = FastAPI(title="AI SecOps Platform")

class LogPayload(BaseModel):
    log_data: str

@app.get("/")
def root():
    return {
        "status": "running",
        "message": "AI SecOps Platform backend is alive 🚀"
    }

@app.post("/detect/ssh")
def detect_ssh(payload: LogPayload):
    events = parse_linux_auth(payload.log_data)
    alerts = detect_ssh_bruteforce(events)

    return {
        "events_parsed": len(events),
        "alerts": alerts
    }
