# packet_filter.py

def packet_matches_filter(packet, protocol=None, src_ip=None, dst_ip=None):
    # Filter by protocol
    if protocol:
        if protocol.upper() == "TCP" and not packet.haslayer("TCP"):
            return False
        elif protocol.upper() == "UDP" and not packet.haslayer("UDP"):
            return False
        elif protocol.upper() == "ICMP" and not packet.haslayer("ICMP"):
            return False

    # Filter by source IP
    if src_ip and packet.haslayer("IP"):
        if packet["IP"].src != src_ip:
            return False

    # Filter by destination IP
    if dst_ip and packet.haslayer("IP"):
        if packet["IP"].dst != dst_ip:
            return False

    return True
