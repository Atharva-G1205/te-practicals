import ipaddress

def display_subnet_info(network):
    # Create an IPv4 network object
    net = ipaddress.IPv4Network(network, strict=False)

    # Network address and Broadcast address
    print(f"\nNetwork Address: {net.network_address}")
    print(f"Broadcast Address: {net.broadcast_address}")
    # Subnet mask
    print(f"Subnet Mask: {net.netmask}")
    
    # Number of usable hosts (excluding network address and broadcast address)
    print(f"Number of Hosts: {net.num_addresses - 2}")
    
    # Host Range (First and Last Usable IP)
    hosts = list(net.hosts())
    print(f"Host Range: {hosts[0]} - {hosts[-1]}")

    new_prefix=int(input("Enter new prefix length for subnetting (e.g., 26): "))

    # Display all possible subnets (e.g., dividing /24 into /26)
    print(f"\nSubnets after dividing /{net.prefixlen} into /{new_prefix}:")
    for subnet in net.subnets(new_prefix=new_prefix):
        print(f"Subnet: {subnet}  Network Address: {subnet.network_address}  Broadcast Address: {subnet.broadcast_address}")
        
# Take network input from user
network_input = input("Enter network (e.g., 192.168.1.0/24): ")

display_subnet_info(network_input)
