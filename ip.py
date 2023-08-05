import sys
import re

"""
判断ip地址是哪一类的IP地址


sample input

225.240.129.203~255.110.255.255
183.181.49.4~255.0.0.0
172.177.113.45~255.0.0.0
176.134.46.246~255.0.0.0
153.63.21.56~255.255.58.255
23.135.167.228~255.0.0.0
204.58.47.149~255.0.0.0
113.33.181.46~255.255.255.0
73.245.52.119~255.255.154.0
23.214.47.71~255.0.0.0
139.124.188.91~255.255.255.100
142.94.192.197~255.0.0.0
53.173.252.202~255.0.0.0
127.201.56.50~255.255.111.255
118.251.84.111~255.0.0.0
130.27.73.170~255.0.0.0
253.237.54.56~255.86.0.0
64.189.222.111~255.255.255.139
148.77.44.147~255.0.0.0
59.213.5.253~255.255.0.0
3.52.119.131~255.255.0.0
213.208.164.145~255.255.0.0
24.22.21.206~255.255.90.255
89.43.34.31~255.0.0.0
9.64.214.75~255.0.0.0
110.156.20.173~255.153.0.0
71.183.242.53~255.255.0.0
119.152.129.100~255.0.0.0
38.187.119.201~255.0.0.0
73.81.221.180~255.255.255.255
73.198.13.199~255.0.15.0
99.42.142.145~255.255.255.0
196.121.115.160~255.0.0.0
226.30.29.206~255.0.0.0
244.248.31.171~255.255.255.255
59.116.159.246~255.0.0.0
121.124.37.157~255.0.0.226
103.42.94.71~255.255.0.0
125.88.217.249~255.255.74.255
73.44.250.101~255.255.255.0
"""
A, B, C, D, E, wrong, private = 0, 0, 0, 0, 0, 0, 0


def parse_ip(ip):
    return tuple(int(i) for i in ip.split('.'))


def valid(mask):
    z = False
    for i in mask:
        for j in range(7, -1, -1):
            if i & (1 << j):
                if z:
                    return False
            else:
                z = True
    if not z:
        return False
    return True


# for line in sys.stdin:
w = []
for line in open('ip.txt').readlines():
    ip, mask = line.strip().split("~")
    if re.match("^\d+\.\d+\.\d+\.\d+$", ip) and re.match("^\d+\.\d+\.\d+\.\d+$", mask):
        pass
    else:
        wrong += 1
        w.append(line)
        continue
    ip = parse_ip(ip)
    mask = parse_ip(mask)
    if ip[0] == 0 or ip[0] == 127:
        continue
    if not valid(mask):
        wrong += 1
        w.append(line)

        continue
    if max(ip) <= 255 and max(mask) <= 255:
        pass
    else:
        wrong += 1
        w.append(line)

        continue

    if ip >= (10, 0, 0, 0) and ip <= (10, 255, 255, 255) or ip >= (172, 16, 0, 0) and ip <= (
    172, 31, 255, 255) or ip >= (192, 168, 0, 0) and ip <= (192, 168, 255, 255):
        private += 1
    if ip >= (1, 0, 0, 0) and ip <= (126, 255, 255, 255):
        A += 1
    elif ip >= (128.0, 0) and ip <= (191, 255, 255, 255):
        B += 1
    elif ip >= (192, 0, 0, 0) and ip <= (223, 255, 255, 255):
        C += 1
    elif ip >= (224, 0, 0, 0) and ip <= (239, 255, 255, 255):
        D += 1
    elif ip >= (240, 0, 0, 0) and ip <= (255, 255, 255, 255):
        E += 1
    else:
        w.append(line)
        wrong += 1

print(A, B, C, D, E, wrong, private)
print(w)