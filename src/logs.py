import os
from datetime import datetime

#define log dir and file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   #fetches absolute path of src/
LOGS_DIR = os.path.join(BASE_DIR, "..", "logs")
LOG_FILE = os.path.join(LOGS_DIR, "logs.txt")

#Ensures that log dir exists
if not os.path.exists(LOGS_DIR):
    os.markirs(LOGS_DIR)

def write_log(timestamp, src_ip, dst_ip, protocol, length):
    #Logs details into txt file
    log_entry = f"[{timestamp}] {protocol} | {src_ip} --> {dst_ip} | Length: {length}\n"

    #write the file
    with open(LOG_FILE, "a") as log:
        log.write(log_entry)