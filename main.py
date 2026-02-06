import sys
import os
import streamlit as st
from verifier import verify_certificate
from confidence import calculate_confidence


sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from fastapi import FastAPI, UploadFile, File
import shutil
from ocr import extract_text
from verifier import verify_certificate
from confidence import calculate_confidence

app = FastAPI()

@app.post("/verify")
async def verify(file: UploadFile = File(...)):
    path = f"temp_{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(path)
    db_score, reasons = verify_certificate(text)
    confidence = calculate_confidence(70, db_score)

    result = "GENUINE" if confidence > 60 else "FAKE"

    return {
        "result": result,
        "confidence": f"{confidence}%",
        "reasons": reasons
    }
