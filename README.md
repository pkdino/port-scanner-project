**Python Port Scanner**

-------
A simple yet powerful Python-based port scanner that identifies open TCP ports on a target host. This project is designed to help cybersecurity enthusiasts and SOC analysts quickly assess network security by identifying exposed services.


🚀 **Features**

- Scans multiple ports for TCP connectivity

- Resolves hostnames to IP addresses

- Provides detailed scan results, including open/closed ports

- User-friendly command-line interface

- Efficient error handling for common networking issues


📦 **Requirements**

- Python 3.x

- Basic understanding of networking and TCP/IP

- Tested on Kali Linux and macOS

- Install required packages (if needed):

- pip install socket



🛠️ **Usage**

Clone the repository and run the script:

git clone https://github.com/your-username/python-port-scanner.git
cd python-port-scanner
python3 port_scanner.py

When prompted, input the target IP address or domain name and a comma-separated list of TCP ports:

*WELCOME TO PORT SCANNER!*

Input a target IP or name of host: example.com
Input ports (comma, separated) or input 'END/end' to exit:
22, 80, 443

Example Output:

*WELCOME TO PORT SCANNER!*

Input a target IP or name of host: scanme.nmap.org
Input ports (comma, separated) or input 'END/end' to exit:
22, 80, 443


📂 Project Structure

.

├── port_scanner.py  # Main Python script

└── README.md        # Project documentation


🔒 Security Note

This tool is intended for ethical use only! Scanning networks without authorization is **ILLEGAL** and against most providers' terms of service. *Use responsibly.*


📜 License

This project is licensed under the MIT License. See the LICENSE file for more information.


🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
