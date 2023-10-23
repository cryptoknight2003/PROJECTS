import scapy.all as scapy

def sniff_packets(interface):
    try:
        # Use the sniff function with the "iface" parameter to specify the network interface.
        scapy.sniff(iface=interface, store=False, prn=process_packet)
    except KeyboardInterrupt:
        print("Packet capture stopped.")

def process_packet(packet):
    # Define your custom packet processing logic here.
    # In this example, we print a summary of each packet.
    print(packet.summary())

if __name__ == "__main__":
    interface = "eth0"  # Replace with the desired network interface
    sniff_packets(interface)
