#Echo Recon

> "Control is an illusion. Recon is real."

Echo Recon is a lightweight and modular reconnaissance tool designed for red teamers and cybersecurity professionals. Built using Python, it automates early-phase information gathering for penetration testing engagements, helping identify surface-level information about targets quickly and efficiently.

# 🔍Features

🕵️ Passive Recon

- WHOIS Lookup
- DNS Enumeration (A, MX, TXT, NS)
- Subdomain Discovery using Public APIs

⚔️ Active Recon

- Port Scanning via Nmap
- Banner Grabbing from Open Ports
- Technology Detection (Wappalyzer-style fingerprinting)

# 🧾Reporting

- Clean and structured HTML report
- Includes timestamps and resolved IPs
- Terminal-based live summary

# ⚙️Modular CLI
- Independent modules callable with flags
- Clean output with color highlighting
- Logging-ready structure with verbosity levels

# 🚀Getting Started

🔧 Installation

#bash

git clone https://github.com/TalhaGurmani/Echo_Recon.git
cd Echo_Recon

#Create and activate a virtual environment

python3 -m venv env
source env/bin/activate

# Install dependencies

pip install -r requirements.txt

# usage 

python recon.py <domain> [options]

for example

python recon.py example.com --whois --dns --subdomains --ports --banner --tech --output report.html

# ⚙️Command-Line Options

| Flag           | Function                                           |
| -------------- | -------------------------------------------------- |
| --whois        | Perform WHOIS lookup                               |
| --dns          | Enumerate DNS records                              |
| --subdomains   | Discover subdomains                                |
| --ports        | Scan open ports                                    |
| --banner       | Grab banners from open ports                       |
| --tech         | Detect technologies used by site                   |
| --output       | Save output report                                 |


# 📸Screenshots

![Screenshot (160)](https://github.com/user-attachments/assets/5da3fab2-aee3-41cf-8bd6-45fafd53cf01)

![Screenshot (161)](https://github.com/user-attachments/assets/87d31ee0-9959-4f56-b788-961e8a1189c0)

![Screenshot (162)](https://github.com/user-attachments/assets/11bb714b-3d36-484e-a33e-4293124fa4bd)

![Screenshot (163)](https://github.com/user-attachments/assets/c380b6e9-af27-4ca1-b014-dca4adb0ba20)

![Screenshot (164)](https://github.com/user-attachments/assets/c2195a8f-4429-47ab-83cb-c2ff224eefad)


# 📚References

OWASP Reconnaissance Guide
Sublist3r
Wappalyzer
Nmap

# ⚠️Disclaimer

This tool is developed for educational and authorized security testing purposes only.
You are responsible for using it ethically and within legal bounds. Do not scan domains or systems without explicit permission.






