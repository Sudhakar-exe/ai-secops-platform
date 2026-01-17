from fastapi import FastAPI

app = FastAPI(title="AI SecOps Platform")

@app.get("/")
def root():
    return {
        "status": "running",
        "message": "AI SecOps Platform backend is alive 🚀"
    }
