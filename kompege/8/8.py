from ipaddress import *

n = ip_network('0.0.0.0/255.255.240.0')
print(n.num_addresses-2)