import ipaddress

for mask in range(33):
    n = ipaddress.ip_network(f'118.193.30.139/{mask}', False)
    if str(n.network_address) == '118.193.24.0':
        print(n.netmask)