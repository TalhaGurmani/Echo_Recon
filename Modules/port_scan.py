# modules/port_scan.py

import nmap

def scan_ports(domain, port_range="1-1000"):
    nm = nmap.PortScanner()
    try:
        nm.scan(domain, port_range, arguments='-sV')
        result = {}
        host = nm.all_hosts()[0] if nm.all_hosts() else None
        if host:
            for proto in nm[host].all_protocols():
                result[proto] = []
                for port in nm[host][proto]:
                    port_info = nm[host][proto][port]
                    result[proto].append({
                        "port": port,
                        "state": port_info["state"],
                        "name": port_info.get("name", ""),
                        "product": port_info.get("product", ""),
                        "version": port_info.get("version", "")
                    })
        return result
    except Exception as e:
        return {"error": str(e)}
