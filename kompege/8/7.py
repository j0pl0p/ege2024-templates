from ipaddress import ip_network

for mask in range(33):
    n = ip_network(f'191.173.145.240/{mask}', False)
    if str(n.network_address) == '191.173.144.0':
        count = 0
        for i in n:
            count += 1
        print(count)