import asyncio
import time
from fastapi import FastAPI, HTTPException

# 🚀 INITIALIZE ENTERPRISE ENGINE: High-performance concurrent REST routing
app = FastAPI(
    title="Aam Janata Swasthya Mitra - Core Engine",
    description="Enterprise Async REST API Routing Infrastructure",
    version="1.0.0"
)

# Mock production medical registry database matrix
DOCTOR_REGISTRY_DATABASE = [
    {"id": 101, "name": "DR. RAHUL SHARMA", "specialty": "CARDIOLOGIST", "location": "Raipur", "is_available": True},
    {"id": 102, "name": "DR. SONY DESAI", "specialty": "SURGEON", "location": "Raipur", "is_available": True},
    {"id": 103, "name": "DR. POOJA MISHRA", "specialty": "PEDIATRICIAN", "location": "Bhilai", "is_available": False}
]

@app.get("/")
async def read_root_health_check():
    """System heartbeat lifeline anchor point"""
    return {
        "status": "ONLINE",
        "system_timestamp": time.time(),
        "engine_integrity": "100% SECURE"
    }

@app.get("/api/v1/doctors/{doctor_id}")
async def fetch_doctor_profile_async(doctor_id: int):
    """
    Asynchronous non-blocking doctor data lookups.
    Simulates a heavy live database query delay using asyncio.sleep.
    """
    print(f"📥 [API Call] Received async fetch request for Doctor ID: {doctor_id}")
    
    # 🔒 THE SENIOR TRICK: Asynchronous non-blocking sleep loop
    # This frees up the server thread to handle other patient incoming calls in parallel!
    await asyncio.sleep(0.2) 
    
    # Linear Single-Pass lookup match matrix
    matched_doctor = next((doc for doc in DOCTOR_REGISTRY_DATABASE if doc["id"] == doctor_id), None)
    
    if matched_doctor is None:
        print(f"❌ [API Error] Doctor ID {doctor_id} not found in master schemas.")
        raise HTTPException(status_code=404, detail="Requested medical practitioner not registered.")
        
    print(f"🟢 [API Success] Extracted structural profile for: {matched_doctor['name']}")
    return {
        "metadata": {"status": "MATCH_VERIFIED", "latency_optimized": True},
        "data": matched_doctor
    }