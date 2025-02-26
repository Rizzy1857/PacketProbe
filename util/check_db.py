import sqlite3
import os

# Define database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "data", "packet_logs.db")

# Function to fetch and display packet logs
def fetch_logs():
    """Fetches and displays all packet logs from the database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Fetch all records from the packets table
        cursor.execute("SELECT * FROM packets")
        logs = cursor.fetchall()

        # Check if database is empty
        if not logs:
            print("[INFO] No logs found in the database.")
            return

        # Print logs in a readable format
        print("\n=== PACKET LOGS ===")
        print("{:<5} | {:<20} | {:<15} -> {:<15} | {:<6} | {:<6}".format(
            "ID", "Timestamp", "Source IP", "Destination IP", "Proto", "Len"))
        print("-" * 80)

        for log in logs:
            print("{:<5} | {:<20} | {:<15} -> {:<15} | {:<6} | {:<6}".format(*log))

    except sqlite3.Error as e:
        print(f"[DB ERROR] Failed to fetch logs: {e}")
    finally:
        conn.close()

# Run the function when script is executed
if __name__ == "__main__":
    fetch_logs()
