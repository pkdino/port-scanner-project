from socket import socket, SOCK_STREAM, AF_INET
from socket import gethostbyname, gethostbyaddr, setdefaulttimeout
import sys
# Socket creates network connections
# SOCK_STREAM uses TCP connections
# AF_INET uses IPv4s

# PortScanner colors
def colorful_ps():
    red     = '\033[91m'
    yellow  = '\033[93m'
    green   = '\033[92m'
    blue    = '\033[94m'
    magenta = '\033[95m'
    cyan    = '\033[96m'
    reset   = '\033[0m'

    p_lines = [
        "██████╗ ",
        "██╔══██╗",
        "██████╔╝",
        "██╔═══╝ ",
        "██║     ",
        "╚═╝     "
    ]

    s_lines = [
        " ██████╗ ",
        "██╔════╝ ",
        "╚█████╗  ",
        " ╚═══██╗ ",
        "██████╔╝ ",
        "╚═════╝  "
    ]

    colors = [red, yellow, green, cyan, blue, magenta]

    print("\n")
    for i in range(len(p_lines)):
        p = colors[i % len(colors)] + p_lines[i] + reset
        s = colors[(i + 2) % len(colors)] + s_lines[i] + reset
        print(f"  {p}   {s}")

# Defining what the port scanner does
def conScan(TgtHost, TgtPort):
    try:
       connskt = socket(AF_INET, SOCK_STREAM)
       connskt.settimeout(1)
       connskt.connect((TgtHost, TgtPort))
       print('[+]%d/tcp open'% TgtPort)
       connskt.close()
    except Exception as e:
        print(f'[-] {TgtPort}/tcp closed ({e})')

# Looking for port, getting host name
def portScan(TgtHost, TgtPort):
    try:
        tgtIP = gethostbyname(TgtHost)
    except Exception as e:
        print(f'[-] Cannot resolve {TgtHost} ({e})')
        return
    
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f'\n[+] Scan result of: {tgtName[0]} ({tgtName})')
    except Exception as e:
        print(f'\n[+] Scan result of: {tgtIP} ({e})')

# Time for python to register port
    setdefaulttimeout(1)
    for port in TgtPort:
        print(f'Scanning Port: {port}')
        conScan(TgtHost, int(port))

# Input a IP/Website name, along with TCP port
if __name__ == '__main__':
    colorful_ps()
    print("\x1B[3mWELCOME TO PORT SCANNER. (ver 1.0)\x1B[0m")
    target = input("Input a target IP or name of host: ").strip()

    while True:
        ports_input = input("Input a port or type 'END/end' to exit: ").strip()

            # Parse and validate port numbers
        ports = [int(p.strip()) for p in ports_input.split(",") if p.isdigit()]

        if ports_input.upper() in ["END"]:
            print("Thank you for using \x1B[3mPORT SCANNER.\x1B[0m")
            print("Goodbye!")
            sys.exit()

        if ports:
            portScan(target, list(map(int, ports)))
        else:
            print("Please enter a \x1B[3mvalid\x1B[0m port number.")
