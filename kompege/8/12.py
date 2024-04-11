from ipaddress import *

count = 0
n = ip_network('10.48.96.0/255.255.240.0')
for i in n:
    s = f'{i:b}'
    if s.count('0') < s.count('1'):
        count += 1
print(count)