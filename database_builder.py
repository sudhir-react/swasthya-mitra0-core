import sqlite3

def initialize_indexed_medical_database():
    print("⚙️ [Database Engine] Initializing physical relational storage vault...")
    
    # Connects and builds a persistent local file named health_registry.db
    connection = sqlite3.connect("health_registry.db")
    cursor = connection.cursor()
    
    # 1. CREATE STRUCTURAL TABLE SCHEMA
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            doctor_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            specialty TEXT NOT NULL,
            location TEXT NOT NULL,
            is_available INTEGER NOT NULL
        )
    """)
    
    # 2. THE SENIOR PERFORMANCE INDEX: Engineering the Binary B-Tree Search Acceleration Vector
    # This optimization forces the database engine to locate the record in O(log N) microsecond operations!
    cursor.execute("""
        CREATE INDEX IF NOT EXISTS idx_doctors_search 
        ON doctors (doctor_id)
    """)
    
    # 3. SEED PRODUCTION DATA ENTRIES (Wiping old rows first to prevent duplicate primary keys)
    cursor.execute("DELETE FROM doctors")
    
    sample_medical_records = [
        (101, "DR. RAHUL SHARMA", "CARDIOLOGIST", "Raipur", 1),
        (102, "DR. SONY DESAI", "SURGEON", "Raipur", 1),
        (103, "DR. POOJA MISHRA", "PEDIATRICIAN", "Bhilai", 0)
    ]
    
    cursor.executemany("""
        INSERT INTO doctors (doctor_id, name, specialty, location, is_available)
        VALUES (?, ?, ?, ?, ?)
    """, sample_medical_records)
    
    # Commit changes permanently to disk matrix and seal boundaries
    connection.commit()
    connection.close()
    print("🟢 [SUCCESS] Relational storage database compiled and B-Tree indexes locked safely!")

if __name__ == "__main__":
    initialize_indexed_medical_database()