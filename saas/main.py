from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path

app = FastAPI(title="saas-ECC")

class Request(BaseModel):
    input: str
    options: dict = {}


@app.get("/health")
def health():
    return {"status": "ok", "service": __name__}

@app.get("/readyz")
def readyz():
    return {"status": "ready", "service": __name__}

@app.get("/")
def home():
    return {"name": "saas-ECC", "description": "The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.", "source": "https://github.com/affaan-m/ECC"}

@app.post("/run")
def run(req: Request):
    # TODO: wrap the actual tool logic here
    return {"status": "prototype", "input": req.input, "message": "Coming soon"}
