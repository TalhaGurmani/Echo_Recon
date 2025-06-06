import requests

def find_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
        subs = {entry['name_value'].strip() for entry in data}
        return sorted(subs)
    except Exception as e:
        return [f"[ERROR] Subdomain enumeration failed: {e}"]
