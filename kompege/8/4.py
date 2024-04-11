from ipaddress import ip_network

for m in range(33):
    n = ip_network(f'122.21.49.91/{m}', False)
    if str(n.network_address) == '122.21.48.0':
        print(n.netmask)

print(bin(240))
