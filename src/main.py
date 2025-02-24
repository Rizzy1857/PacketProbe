from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    # Checks if the packet has an IP layer
    if IP in packet:
        proto = ''
        if TCP in packet:
            proto = 'TCP'           #for TCP in packet
        elif UDP in packet:
            proto = 'UDP'           #for UDP in packet
        elif ICMP in packet:
            proto = 'ICMP'          #for ICMP in packet
        else:
            proto = 'OTHER'         #if none above is the one
        
        # Print packet details
        print(f"[{proto}] {packet[IP].src} --> {packet[IP].dst}")

def main():
    print("NetSleuth v1.0 - Network Sniffer is running... (Press Ctrl+C to stop)")
    try:
        sniff(prn=packet_callback, store=False)
    except KeyboardInterrupt:
        print("\n[!] Sniffer stopped by user.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()
