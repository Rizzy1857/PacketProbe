# PacketProbe v1.0

A **simple yet powerful network sniffer** built with Python using **Scapy**. It captures real-time network packets and displays source/destination IPs along with the protocol used (TCP/UDP/ICMP). Ideal for beginners diving into network security and packet analysis.

---

##  Features

-  **Sniffs network traffic** in real-time
-  **Displays IP addresses** (source & destination)
-  **Detects protocols:** TCP, UDP, ICMP, and others
-  **Lightweight & beginner-friendly**

# PacketProbe v1.1 - Changelog & Features

## New Features & Improvements

### Packet Filtering
- Users can now filter packets based on **protocol (TCP/UDP/ICMP), source IP, and destination IP**.
- Implemented through `packet_filter.py`, ensuring cleaner and more precise packet capture.

### Logging System
- **Raw logs** are now stored in `logs/logs.txt` for easy review.
- Logs include **timestamp, source IP, destination IP, protocol, and packet length**.

### Database Integration
- Introduced **SQLite-based packet logging** (`packet_logs.db` in `data/`).
- **All captured packets are logged into a structured database** for better analysis and retrieval.
- `db_handler.py` manages database operations (**storing logs, ensuring table structure**).

### Database Log Viewer (`check_db.py`)
- Easily retrieve and display stored packet logs in a **formatted table**.
- Prevents crashes with **error handling & empty database checks**.

---

## How to Use

### Run the Packet Sniffer
```bash
python main.py --protocol TCP
```
*(Modify filters as needed: `--protocol UDP` or `--src-ip 192.168.1.1`)*

### View Logs (Raw TXT Format)
```bash
cat logs/logs.txt
```

### Check Stored Logs in Database
```bash
python check_db.py
```
*(Displays packets in a table format from `packet_logs.db`.)*

---

##  Requirements

1. **Python 3.x**  → [Download Python](https://www.python.org/downloads/)
2. **Scapy** (for packet capturing)
3. **Npcap** (to capture network packets on Windows)

---

##  Installation Guide

### ✅ **1. Install Python & PIP**
- Download & install **Python 3.x** from [python.org](https://www.python.org/downloads/).
- Ensure **pip** is added to your system PATH during installation.

### ✅ **2. Install Dependencies**
Open **Command Prompt** and run:

```bash
pip install scapy
```

### ✅ **3. Install Npcap (Windows Only)**
- Download **Npcap** → [Npcap Download](https://nmap.org/npcap/)
- **Run as Administrator** and during installation:
  - ✅ *Check* → "Install Npcap in WinPcap API-compatible Mode"

###  **Why Npcap?**
Npcap is essential for Scapy to access network interfaces and sniff packets on Windows. Without it, the sniffer won’t run.

---

##  Running PacketProbe

1. **Run Command Prompt as Administrator** (Windows)
2. Navigate to the project folder:

```bash
cd path\to\PacketProbe
```

3. **Run the sniffer:**

```bash
python main.py
```

4. **To stop the sniffer:** Press **Ctrl + C**

---

##  Sample Output

```
PacketProbe v1.0 - Network Sniffer is running... (Press Ctrl+C to stop)
[TCP] 192.168.1.5 --> 142.250.182.206
[UDP] 192.168.1.5 --> 8.8.8.8
[ICMP] 192.168.1.5 --> 8.8.8.8
[!] Sniffer stopped by user.
```

---

##  Troubleshooting

- **WinPcap/Npcap Error?** → Ensure **Npcap** is installed in *WinPcap-compatible mode*.
- **No Packets Showing?** → Run the script as **Administrator**.
- **Still stuck?** → Check firewall settings or try generating traffic (e.g., `ping google.com`).

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

 **Disclaimer! Made for educational pourpose only.** 🚀
