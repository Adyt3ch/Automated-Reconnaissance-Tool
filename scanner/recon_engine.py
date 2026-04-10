import socket
import requests
import concurrent.futures
from urllib.parse import urljoin

class ReconScanner:
    def __init__(self, target):
        self.target = target
        try:
            self.target_ip = socket.gethostbyname(target)
        except socket.gaierror:
            self.target_ip = None

    def scan_port(self, port, detect_services=False):
        """Scans a single port. If detect_services is True, grabs banner."""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)
            result = s.connect_ex((self.target_ip, port))
            
            banner = "N/A"
            is_open = False

            if result == 0:
                is_open = True
                if detect_services:
                    try:
                        # Simple Banner Grab
                        s.send(b'HEAD / HTTP/1.0\r\n\r\n')
                        banner = s.recv(1024).decode().strip()
                    except:
                        banner = "Unknown Service"
            
            s.close()
            return port, is_open, banner
        except:
            return port, False, None

    def run_port_scan(self, detect_services=False):
        """Threaded Port Scan. Accepts flag to toggle service detection."""
        if not self.target_ip:
            return []
        
        # Standard Top Ports
        ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 8080]
        open_ports = []
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # Pass the detect_services flag to the worker
            future_to_port = {executor.submit(self.scan_port, port, detect_services): port for port in ports}
            
            for future in concurrent.futures.as_completed(future_to_port):
                port, is_open, banner = future.result()
                if is_open:
                    open_ports.append({'port': port, 'service': banner})
        
        return sorted(open_ports, key=lambda x: x['port'])

    # (check_headers and dir_bruteforce methods remain the same as previous)
    def check_headers(self):
        target_url = f"http://{self.target}"
        security_headers = ['X-Frame-Options', 'X-XSS-Protection', 'Content-Security-Policy']
        results = {}
        try:
            res = requests.get(target_url, timeout=3)
            for h in security_headers:
                results[h] = res.headers.get(h, "MISSING ❌")
        except:
            results['Error'] = "Connection Failed"
        return results

    def dir_bruteforce(self):
        wordlist = ['admin', 'login', 'dashboard', 'uploads', 'config']
        found_dirs = []
        base_url = f"http://{self.target}"
        try:
            for path in wordlist:
                url = urljoin(base_url, path)
                res = requests.get(url, timeout=2)
                if res.status_code == 200:
                    found_dirs.append(f"/{path} (200 OK)")
        except:
            pass
        return found_dirs