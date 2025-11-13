import socket

def dns_lookup():
    while True:
        print("DNS Lookup Tool")
        print("1. Find IP address from domain name")
        print("2. Find domain name from IP address")
        choice = input("Enter choice (1 or 2): ").strip()

        if choice == '1':
            domain = input("Enter domain name (e.g., example.com): ").strip()
            try:
                ip_address = socket.gethostbyname(domain)
                print(f"The IP address of {domain} is: {ip_address}")
            except socket.gaierror:
                print("Error: Unable to resolve domain name.")

        elif choice == '2':
            ip_address = input("Enter IP address (e.g., 8.8.8.8): ").strip()
            try:
                domain_name = socket.gethostbyaddr(ip_address)
                print(f"The domain name for {ip_address} is: {domain_name[0]}")
            except socket.herror:
                print("Error: Unable to resolve IP address.")

        elif choice=='3':
            print("exitinggg")
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    dns_lookup()


