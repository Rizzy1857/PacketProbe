import argparse
from scapy.all import sniff, IP
from packet_filter import packet_matches_filter

# Mapping protocol numbers to readable names
PROTOCOLS = {
    1: "ICMP",
    6: "TCP",
    17: "UDP"
}

def packet_callback(packet):
#Prints the protocol name instead of numbers [6] for TCP, [17] UDP
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        proto_num = ip_layer.proto
        proto_name = PROTOCOLS.get(proto_num, f"Unknown({proto_num})")
        print(f"[{proto_name}] {ip_layer.src} --> {ip_layer.dst}")

def main():
    parser = argparse.ArgumentParser(description="NetSleuth - A Simple Network Sniffer with Filtering")
    parser.add_argument("--protocol", help="Filter by protocol (TCP, UDP, ICMP)")
    parser.add_argument("--src-ip", help="Filter by source IP address")
    parser.add_argument("--dst-ip", help="Filter by destination IP address")
    args = parser.parse_args()

    print("Starting packet capture... Press Ctrl+C to stop.")

    # Start sniffing with filtering applied
    sniff(prn=lambda pkt: packet_callback(pkt) if packet_matches_filter(pkt, args.protocol, args.src_ip, args.dst_ip) else None, store=False)

if __name__ == "__main__":
    main()
