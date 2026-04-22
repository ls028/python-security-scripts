import socket

PORT_NAMES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt"
}

def scan_ports(target, ports):
    print(f"\nScanning {target}...\n")
    open_ports = []
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                service = PORT_NAMES.get(port, "Unknown")
                print(f"Port {port}: OPEN ({service})")
                open_ports.append(port)
            sock.close()
        except socket.gaierror:
            print(f"Could not resolve hostname: {target}")
            break
        except socket.error:
            print(f"Connection error on port {port}")

    print(f"\nScan complete. {len(open_ports)} open port(s) found.")

target = input("Enter target IP or hostname: ")
ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 3389, 8080]
scan_ports(target, ports)
