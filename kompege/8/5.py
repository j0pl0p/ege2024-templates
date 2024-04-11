from ipaddress import ip_network

for mask in range(33):
    n = ip_network(f'173.103.25.118/{mask}', False)
    if str(n.network_address) == '173.103.24.0':
        print(32 - mask)