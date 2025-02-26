import sqlite3
import os
from tabulate import tabulate  # For structured output

# Define the database path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "data", "packet_logs.db")

def query_packets(filter_column=None, filter_value=None):
    #Queries packets from the database with optional filtering.
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    query = "SELECT id, timestamp, src_ip, dst_ip, protocol, length FROM packets"
    params = ()
    
    if filter_column and filter_value:
        query += f" WHERE {filter_column} = ?"
        params = (filter_value,)
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    
    return rows

def display_results(rows):
    #Displays the query results in a structured table.
    headers = ["ID", "Timestamp", "Source IP", "Destination IP", "Protocol", "Length"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))

def interactive_query():
    #Interactive query mode for user-friendly filtering.
    
    print("\nPacket Query Tool - Select a filter:")
    print("1. View all packets")
    print("2. Filter by source IP")
    print("3. Filter by destination IP")
    print("4. Filter by protocol (TCP, UDP, ICMP)")
    print("5. Filter by packet length")
    choice = input("Enter choice (1-5): ")
    
    filters = {
        "2": "src_ip",
        "3": "dst_ip",
        "4": "protocol",
        "5": "length"
    }
    
    if choice == "1":
        results = query_packets()
    elif choice in filters:
        value = input(f"Enter {filters[choice]} value: ")
        results = query_packets(filters[choice], value)
    else:
        print("Invalid choice.")
        return
    
    display_results(results)

if __name__ == "__main__":
    interactive_query()
