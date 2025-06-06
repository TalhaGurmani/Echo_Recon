import whois

def lookup(domain):
    try:
        return str(whois.whois(domain))
    except Exception as e:
        return f"[ERROR] WHOIS failed: {e}"
