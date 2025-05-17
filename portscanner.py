from socket import socket, SOCK_STREAM, AF_INET
from socket import gethostbyname, gethostbyaddr, setdefaulttimeout
# Socket creates network connections
# SOCK_STREAM uses TCP connections
# AF_INET uses IPv4s

# defining what the port scanner does
def conScan(TgtHost, TgtPort):
    try:
       connskt = socket(AF_INET, SOCK_STREAM)
       connskt.settimeout(1)
       connskt.connect((TgtHost, TgtPort))
       print('[+]%d/tcp open'% TgtPort)
       connskt.close()
    except Exception as e:
        print(f'[-] {TgtPort}/tcp closed ({e})')

# looking for port, getting host name
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

# time for python to register port
    setdefaulttimeout(1)
    for port in TgtPort:
        print(f'Scanning Port: {port}')
        conScan(TgtHost, int(port))

# input a IP/Website name, along with TCP port
if __name__ == '__main__':
    print("\x1B[3mWELCOME TO PORT SCANNER!\x1B[0m")
    target = input("Input a target IP or name of host: ").strip()

    while True:
        ports_input = input("Input ports (comma, separated) or input 'END/end' to exit: ")

        

        ports = [int(p.strip()) for p in ports_input.split(",") if p.isdigit()]

        if ports:
            portScan(target, list(map(int, ports)))
        else:
            print("Please enter \x1B[3mvalid\x1B[0m port numbers.")

            portScan(input(), [22, 80, 443,])

        if ports_input.upper() in ["END"]:
            print("Thank you for using \x1B[3mPORT SCANNER.\x1B[0m")
            break

    portScan(input(), [22, 80, 443,])