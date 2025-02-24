# PacketProbe v1.0

A **simple yet powerful network sniffer** built with Python using **Scapy**. It captures real-time network packets and displays source/destination IPs along with the protocol used (TCP/UDP/ICMP). Ideal for beginners diving into network security and packet analysis.

---

##  Features

-  **Sniffs network traffic** in real-time
-  **Displays IP addresses** (source & destination)
-  **Detects protocols:** TCP, UDP, ICMP, and others
-  **Lightweight & beginner-friendly**

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

- ** WinPcap/Npcap Error?** → Ensure **Npcap** is installed in *WinPcap-compatible mode*.
- ** No Packets Showing?** → Run the script as **Administrator**.
- **Still stuck?** → Check firewall settings or try generating traffic (e.g., `ping google.com`).

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

 **Disclaimer! Made for educational pourpose only.** 🚀
