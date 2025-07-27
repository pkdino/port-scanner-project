# 🔍 Port Scanner (v1.0)

**This project is for educational and ethical use only. Please use responsibly.**

Welcome to my custom **TCP Port Scanner**, built with Python!  
This tool performs basic network reconnaissance by scanning user-specified TCP ports on a given target IP or hostname.
As part of my journey into cybersecurity and SOC analysis, I wanted to understand how basic port scanning works under the hood. Writing this from scratch helped me strengthen my skills in:

- TCP/IP networking
- Python socket programming
- Reconnaissance and enumeration techniques

---

## 🎯 Features

- Accepts a domain name or IP address as input
- Scans one or more TCP ports for open/closed status
- Uses Python's `socket` library to initiate TCP connections
- Displays the resolved hostname and IP (if available)
- Gracefully handles DNS resolution errors and timeouts
- Includes a colorful ASCII-art banner for a fun CLI experience

---

## 🛠 Technologies Used

- Python 3
- `socket` module (`AF_INET`, `SOCK_STREAM`)
- DNS resolution (`gethostbyname`, `gethostbyaddr`)
- Command-line input parsing

---

## 🚀 How to Run

1. **Clone the repository**
in bash:
->git clone https://github.com/pkdino/port-scanner-project.git
-> cd port-scanner-project

2. **Run the scanner**
-> python3 portscanner.py

3. **Example Usage**
Input a target IP or name of host: scanme.nmap.org
*|* Input a port or type 'END/end' to exit: 22, 80, 443

**This project is for educational and ethical use only. Please use responsibly.**
