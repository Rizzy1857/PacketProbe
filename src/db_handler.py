import sqlite3
import os

# Define database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "data", "packet_logs.db")

# Create or connect to the database and initialize the table
def init_db():
    #Initializes the database by creating the packets table if it does not exist.
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS packets (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                src_ip TEXT NOT NULL,
                dst_ip TEXT NOT NULL,
                protocol TEXT NOT NULL,
                length INTEGER NOT NULL
            )
        ''')
        conn.commit()
    except sqlite3.Error as e:
        print(f"[DB ERROR] Failed to initialize database: {e}")
    finally:
        conn.close()

# Log each packet into the database
def log_packet(timestamp, src_ip, dst_ip, protocol, length):
    #Inserts a new packet log into the database.
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO packets (timestamp, src_ip, dst_ip, protocol, length)
            VALUES (?, ?, ?, ?, ?)
        ''', (timestamp, src_ip, dst_ip, protocol, length))
        conn.commit()
    except sqlite3.Error as e:
        print(f"[DB ERROR] {e}")
    finally:
        conn.close()

# Ensure the database is initialized when the script is imported
init_db()
