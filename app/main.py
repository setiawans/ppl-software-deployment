"""
PPL C - Steven Setiawan
Minimal FastAPI app for deployment PoC.
"""

import os
from fastapi import FastAPI

app = FastAPI(title="PPL C Deploy PoC")

APP_VERSION = os.getenv("APP_VERSION", "v1.0.0")
APP_COLOR = os.getenv("APP_COLOR", "blue")
APP_ENV = os.getenv("APP_ENV", "dev")


@app.get("/")
def root():
    return {
        "message": "PPL C - Steven Setiawan",
        "version": APP_VERSION,
        "color": APP_COLOR,
        "environment": APP_ENV,
    }


@app.get("/health")
def health():
    """Liveness & readiness probe endpoint buat Kubernetes."""
    return {"status": "ok"}
