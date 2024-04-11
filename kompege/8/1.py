import ipaddress

n = ipaddress.ip_network('10.8.248.131/255.255.224.0', False)
print(n.network_address)