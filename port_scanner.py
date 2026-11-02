import socket
import sys

target_host = "127.0.0.1"
ports_to_scan = [80, 443, 22, 21, 23]

print(f"=== Scanning target: {target_host} ===")

for port in ports_to_scan:
    try:
        s = socket.socket(socket.AF_INET, socket.socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_host, port))
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        else:
            print(f"[-] Port {port}: Closed")
        s.close()
    except socket.error:
        print(f"Could not connect to port {port}")
        sys.exit()

print("=== Scan Completed ===")
