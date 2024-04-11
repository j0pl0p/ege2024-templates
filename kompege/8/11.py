from ipaddress import *

count = 0
n = ip_network('192.168.240.0/255.255.255.0')
for i in n:
    s = str(bin(int(i)))[2:]
    if s.count('0') == s.count('1'):
        count += 1
print(count)