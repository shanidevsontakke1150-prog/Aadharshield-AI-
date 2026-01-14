import sqlite3
from datetime import datetime

DB_NAME = "events.db"

def log_event(aadhaar_id, location, device, service, risk, reason):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aadhaar_id TEXT,
            location TEXT,
            device TEXT,
            service TEXT,
            risk TEXT,
            reason TEXT,
            time TEXT
        )
    """)

    c.execute("""
        INSERT INTO events (aadhaar_id, location, device, service, risk, reason, time)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (aadhaar_id, location, device, service, risk, reason, datetime.utcnow().isoformat()))

    conn.commit()
    conn.close()
