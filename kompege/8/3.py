from ipaddress import ip_network

for mask in range(33):
    n = ip_network(f'154.201.208.17/{mask}', False)
    if str(n.network_address) == '154.201.192.0':
        print(n.netmask)