import sqlite3
import os
from datetime import datetime

# Define DB path
DB_PATH = os.path.join('data', 'packetprobe.db')

def initialize_db():
    """Create the database and the packets table if they don't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS packets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            source_ip TEXT,
            destination_ip TEXT,
            protocol TEXT,
            length INTEGER
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

def log_packet(timestamp, source_ip, destination_ip, protocol, length):
    """Insert a captured packet into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO packets (timestamp, source_ip, destination_ip, protocol, length)
        VALUES (?, ?, ?, ?, ?)
    ''', (timestamp, source_ip, destination_ip, protocol, length))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
