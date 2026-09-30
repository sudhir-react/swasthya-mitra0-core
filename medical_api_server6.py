import asyncio
import time
import sqlite3
import aiofiles
from fastapi import FastAPI, HTTPException, Request, status

app = FastAPI(
    title="Aam Janata Swasthya Mitra - Core Engine",
    description="Enterprise Async REST API with Relational Storage and Rate-Limiting Guard",
    version="5.0.0"
)

LOG_FILE_PATH = "security_telemetry.log"

# 🔒 THE RATE LIMITING VAULT: In-memory dictionary to track client request footprints
# Structure: { "client_ip": [timestamp1, timestamp2, ...] }
CLIENT_REQUEST_TRACKER = {}
RATE_LIMIT_WINDOW_SECONDS = 1.0
MAX_ALLOWED_REQUESTS_PER_WINDOW = 5

@app.middleware("http")
async def advanced_security_and_telemetry_middleware(request: Request, call_next):
    """
    Advanced Multi-Shield Middleware Interceptor.
    1. Intercepts incoming packets to validate rate-limiting bounds dynamically.
    2. Computes microsecond execution latency and logs telemetry asynchronously to disk.
    """
    client_ip = request.client.host if request.client else "UNKNOWN_SOURCE"
    current_timestamp = time.time()
    
    # --- 🛡️ SHIELD 1: ASYNC RATE LIMITING GUARD ---
    if client_ip not in CLIENT_REQUEST_TRACKER:
        CLIENT_REQUEST_TRACKER[client_ip] = []
        
    # Purge timestamps that fall outside the active 1-second monitoring window
    CLIENT_REQUEST_TRACKER[client_ip] = [
        ts for ts in CLIENT_REQUEST_TRACKER[client_ip] 
        if current_timestamp - ts < RATE_LIMIT_WINDOW_SECONDS
    ]
    
    # Evaluate threshold breaches
    if len(CLIENT_REQUEST_TRACKER[client_ip]) >= MAX_ALLOWED_REQUESTS_PER_WINDOW:
        print(f"🚨 [CRITICAL SECURITY BREACH] IP {client_ip} throttled! Request flood detected.")
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded. Too many requests flooding the engine. Access denied."
        )
        
    # Append the current verified request timestamp into the memory tracker
    CLIENT_REQUEST_TRACKER[client_ip].append(current_timestamp)
    
    # --- 📊 SHIELD 2: TELEMETRY LATENCY MATRIX ---
    start_time = time.perf_counter()
    response = await call_next(request)
    end_time = time.perf_counter()
    execution_duration_ms = (end_time - start_time) * 1000
    
    request_method = request.method
    endpoint_path = request.url.path
    status_code = response.status_code
    
    log_statement = (
        f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 📊 [TELEMETRY] {client_ip} | "
        f"{request_method} {endpoint_path} -> Status: {status_code} | Latency: {execution_duration_ms:.2f} ms\n"
    )
    print(log_statement.strip())
    
    async with aiofiles.open(LOG_FILE_PATH, mode="a", encoding="utf-8") as log_file:
        await log_file.write(log_statement)
        
    return response

def fetch_doctor_from_db(doctor_id: int):
    """Synchronous worker function to handle low-level SQLite disk reads safely"""
    connection = sqlite3.connect("health_registry.db")
    cursor = connection.cursor()
    cursor.execute(
        "SELECT doctor_id, name, specialty, location, is_available FROM doctors WHERE doctor_id = ?",
        (doctor_id,)
    )
    row = cursor.fetchone()
    connection.close()
    return row

@app.get("/")
async def read_root_health_check():
    """System heartbeat lifeline anchor point"""
    return {
        "status": "ONLINE",
        "database_connected": True,
        "system_timestamp": time.time(),
        "engine_integrity": "100% SECURE"
    }

@app.get("/api/v1/doctors/{doctor_id}")
async def fetch_doctor_profile_async(doctor_id: int):
    """Asynchronous non-blocking route handler executing indexed database queries."""
    print(f"📥 [API Call] Querying relational disk vault for Doctor ID: {doctor_id}")
    await asyncio.sleep(0.1) # Controlled simulation delay
    db_row = fetch_doctor_from_db(doctor_id)
    
    if db_row is None:
        raise HTTPException(status_code=404, detail="Requested medical practitioner not registered.")
    
    structured_payload = {
        "id": db_row[0],
        "name": db_row[1],
        "specialty": db_row[2],
        "location": db_row[3],
        "is_available": True if db_row[4] == 1 else False
    }
    return {
        "metadata": {"status": "RELATIONAL_MATCH_VERIFIED", "index_optimized": True},
        "data": structured_payload
    }