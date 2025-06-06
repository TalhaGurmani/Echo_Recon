import argparse
from datetime import datetime
from modules import whois_lookup, dns_enum, subdomain_enum, port_scan, banner_grab, tech_detect
from colorama import Fore, Style, init as colorama_init

colorama_init(autoreset=True)

def print_banner():
    print(f"{Fore.CYAN}{Style.BRIGHT}\n" + "=" * 60)
    print(f"{' ' * 18}Echo Recon   v1.0")
    print("=" * 60 + Style.RESET_ALL)
    print(f"{Fore.YELLOW}\"Control is an illusion. Recon is real.\" — Echo Recon\n{Style.RESET_ALL}")

def pretty_print(section, content):
    print(f"\n{Fore.GREEN}[+] {section}:\n{Fore.WHITE}{'-'*60}")
    if isinstance(content, dict):
        for k, v in content.items():
            if isinstance(v, list):
                print(f"{Fore.CYAN}{k}:")
                for item in v:
                    print(f" └ {item}")
            else:
                print(f"{k}: {v}")
    elif isinstance(content, list):
        for item in content:
            print(f" └ {item}")
    else:
        print(content)
    print('-' * 60)

def html_section(title, content):
    html = f"<h2>{title}</h2><pre>"
    if isinstance(content, dict):
        for k, v in content.items():
            html += f"{k}:\n"
            if isinstance(v, list):
                for item in v:
                    html += f"  - {item}\n"
            else:
                html += f"  {v}\n"
    elif isinstance(content, list):
        for item in content:
            html += f"- {item}\n"
    else:
        html += str(content)
    html += "</pre><hr>"
    return html

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="Echo Recon - Modular Reconnaissance CLI Tool")
    parser.add_argument("domain", help="Target domain")
    parser.add_argument("--whois", action="store_true", help="Perform WHOIS lookup")
    parser.add_argument("--dns", action="store_true", help="Enumerate DNS records")
    parser.add_argument("--subdomains", action="store_true", help="Find subdomains")
    parser.add_argument("--ports", action="store_true", help="Scan common ports")
    parser.add_argument("--banner", action="store_true", help="Grab banners from open ports")
    parser.add_argument("--tech", action="store_true", help="Detect technologies")
    parser.add_argument("--output", default="sample_report.html", help="Output report filename")
    args = parser.parse_args()

    report_data = {}
    domain = args.domain
    html_report = f"<html><head><title>Echo Recon Report</title></head><body>"
    html_report += f"<h1>Echo Recon Report for {domain}</h1><p><b>Generated:</b> {datetime.now()}</p><hr>"

    if args.whois:
        print(f"{Fore.BLUE}[+] Running WHOIS lookup...")
        result = whois_lookup.lookup(domain)
        pretty_print("WHOIS", result)
        html_report += html_section("WHOIS", result)
        report_data['WHOIS'] = result

    if args.dns:
        print(f"{Fore.BLUE}[+] Running DNS enumeration...")
        result = dns_enum.enumerate(domain)
        pretty_print("DNS Records", result)
        html_report += html_section("DNS Records", result)
        report_data['DNS'] = result

    if args.subdomains:
        print(f"{Fore.BLUE}[+] Searching for subdomains...")
        result = subdomain_enum.find_subdomains(domain)
        pretty_print("Subdomains", result)
        html_report += html_section("Subdomains", result)
        report_data['Subdomains'] = result

    if args.ports:
        print(f"{Fore.BLUE}[+] Scanning ports...")
        result = port_scan.scan_ports(domain)
        pretty_print("Open Ports", result)
        html_report += html_section("Open Ports", result)
        report_data['Ports'] = result

    if args.banner:
        ports_to_scan = []
        if 'Ports' in report_data:
            ports_to_scan = [
                entry["port"] for entries in report_data['Ports'].values()
                for entry in entries if entry["state"] == "open"
            ]
        else:
            ports_to_scan = [80, 443]

        print(f"{Fore.BLUE}[+] Grabbing banners from ports: {ports_to_scan}")
        banners = {port: banner_grab.grab(domain, port) for port in ports_to_scan}
        pretty_print("Banners", banners)
        html_report += html_section("Banners", banners)
        report_data['Banners'] = banners

    if args.tech:
        print(f"{Fore.BLUE}[+] Detecting technologies...")
        result = tech_detect.detect(domain)
        pretty_print("Technologies", result)
        html_report += html_section("Technologies", result)
        report_data['Technologies'] = result

    html_report += "</body></html>"

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(html_report)

    print(f"\n{Fore.GREEN}[+] Report saved to {args.output}")

if __name__ == "__main__":
    main()
