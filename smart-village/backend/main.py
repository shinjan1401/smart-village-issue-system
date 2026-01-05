from fastapi import FastAPI, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os, uuid

app = FastAPI()
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
import uuid

app = FastAPI()

# ---------- STATIC FILES SETUP ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "uploads")

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")
# --------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

issues = []

import os

@app.post("/add")
async def add_issue(
    desc: str = Form(...),
    photo: UploadFile = File(...)
):
    safe_name = photo.filename.replace(" ", "_")
    filename = f"before_{uuid.uuid4()}_{safe_name}"
    path = f"{UPLOAD_DIR}/{filename}"

    with open(path, "wb") as f:
        f.write(await photo.read())

    issue = {
        "id": len(issues) + 1,
        "desc": desc,
        "photo": filename,
        "status": "Pending"
    }

    issues.append(issue)
    return issue

@app.get("/issues")
def get_issues():
    return issues
@app.post("/complete/{issue_id}")
async def complete_issue(
    issue_id: int,
    photo: UploadFile = File(...)
):
    safe_name = photo.filename.replace(" ", "_")
    filename = f"after_{uuid.uuid4()}_{safe_name}"
    path = f"{UPLOAD_DIR}/{filename}"

    with open(path, "wb") as f:
        f.write(await photo.read())

    for issue in issues:
        if issue["id"] == issue_id:
            issue["after_photo"] = filename
            issue["status"] = "Waiting Approval"
            return {"ok": True}

    return {"error": "Issue not found"}

@app.post("/approve/{issue_id}")
def approve_issue(issue_id: int):
    for issue in issues:
        if issue["id"] == issue_id:
            issue["status"] = "Completed & Approved"
            return {"ok": True}
    return {"error": "Issue not found"}

@app.get("/")
def root():
    return {"message": "Smart Village Backend Running"}

