import argparse
from scapy.all import sniff, IP
from packet_filter import packet_matches_filter
from db_handler import log_packet 

# Mapping protocol numbers to readable names
PROTOCOLS = {
    1: "ICMP",
    6: "TCP",
    17: "UDP"
}

def packet_callback(packet, args):
#Prints the protocol name instead of numbers [6] for TCP, [17] UDP
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        proto_num = ip_layer.proto
        proto_name = PROTOCOLS.get(proto_num, f"Unknown({proto_num})")

        # Apply filters
        if packet_matches_filter(packet, args.protocol, args.src_ip, args.dst_ip):
            print(f"[{proto_name}] {ip_layer.src} --> {ip_layer.dst}")

            # Log packet into the database
            log_packet(
                timestamp=str(packet.time),
                src_ip=ip_layer.src,
                dst_ip=ip_layer.dst,
                protocol=proto_name
            )

def main():
    parser = argparse.ArgumentParser(description="PacketProbe - Network Sniffer with Filtering & Logging")
    parser.add_argument("--protocol", help="Filter by protocol (TCP, UDP, ICMP)")
    parser.add_argument("--src-ip", help="Filter by source IP address")
    parser.add_argument("--dst-ip", help="Filter by destination IP address")
    args = parser.parse_args()

    print("Starting packet capture... Press Ctrl+C to stop.")

    # Start sniffing with filtering and logging
    sniff(prn=lambda pkt: packet_callback(pkt, args), store=False)

if __name__ == "__main__":
    main()
