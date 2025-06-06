import socket

def grab(domain, port):
    try:
        with socket.create_connection((domain, port), timeout=3) as s:
            s.send(b'HEAD / HTTP/1.0\r\n\r\n')
            return s.recv(1024).decode(errors='ignore').strip()
    except Exception as e:
        return f"[ERROR] {e}"
