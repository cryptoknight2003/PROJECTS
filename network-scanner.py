import argparse
import socket
import threading
from datetime import datetime

def scan_port(target, port, timeout):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
            # Add banner grabbing code here if desired
        sock.close()
    except (socket.timeout, ConnectionRefusedError):
        pass

def port_scan(target, ports, max_threads, timeout):
    try:
        ip = socket.gethostbyname(target)
        print("-" * 50)
        print(f"Scanning target: {ip}")
        print("Time started:", datetime.now())
        print("-" * 50)

        for port in ports:
            thread = threading.Thread(target=scan_port, args=(ip, port, timeout))
            thread.start()
            if threading.active_count() >= max_threads:
                thread.join()

        # Wait for any remaining threads to finish
        for thread in threading.enumerate():
            if thread != threading.current_thread():
                thread.join()

    except socket.gaierror:
        print("Hostname could not be resolved.")
    except socket.error:
        print("Could not connect to the server.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Improved Port Scanner")
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("-p", "--ports", default="1-100", help="Port range to scan (e.g., 1-100)")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Maximum concurrent threads")
    parser.add_argument("-timeout", "--timeout", type=float, default=1, help="Connection timeout in seconds")
   
