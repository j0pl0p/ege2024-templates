from ipaddress import ip_network

count = 0
for mask in range(33):
    n = ip_network(f'158.116.11.146/{mask}', False)
    if str(n.network_address) == '158.116.0.0':
        count += 1

print(count)