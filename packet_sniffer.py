from scapy.all import sniff

def process_packet(packet):
    print(packet.summary())

print("=" * 50)
print("        BASIC NETWORK SNIFFER")
print("=" * 50)
print("Capturing packets... Press Ctrl+C to stop.\n")

try:
    sniff(prn=process_packet, store=False)
except KeyboardInterrupt:
    print("\nSniffing stopped.")