from socket import socket, SOCK_STREAM, AF_INET, gethostbyname, gethostbyaddr, setdefaulttimeout
import sys
import time

def slow_print(text, delay=0.07):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

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

def conScan(TgtHost, TgtPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.settimeout(1)
        connskt.connect((TgtHost, TgtPort))
        slow_print('[+] %d/tcp open' % TgtPort)
        connskt.close()
    except Exception as e:
        slow_print(f'[-] {TgtPort}/tcp closed ({e})')

def portScan(TgtHost, TgtPort):
    try:
        tgtIP = gethostbyname(TgtHost)
    except Exception as e:
        slow_print(f'[-] Cannot resolve {TgtHost} ({e})')
        return
    
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f'\n[+] Scan result of: {tgtName[0]} ({tgtName})')
    except Exception as e:
        print(f'\n[+] Scan result of: {tgtIP} ({e})')

    setdefaulttimeout(1)
    for port in TgtPort:
        print(f'Scanning Port: {port}')
        conScan(TgtHost, int(port))

if __name__ == '__main__':
    colorful_ps()
    slow_print("\x1B[3mWELCOME TO PORT SCANNER. (ver 1.1)\x1B[0m")
    target = input("Input a target IP or name of host: ").strip()

    while True:
        ports_input = input("Input a port or type 'END/end' to exit: ").strip()

        if ports_input.upper() == "END":
            slow_print("Thank you for using \x1B[3mPORT SCANNER.\x1B[0m")
            slow_print("Goodbye!")
            sys.exit()

        ports = [int(p.strip()) for p in ports_input.split(",") if p.strip().isdigit()]

        if ports:
            portScan(target, ports)
        else:
            print("Please enter a \x1B[3mvalid\x1B[0m port number.")
