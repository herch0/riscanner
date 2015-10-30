#41.87.128.0	41.87.159.255

from urllib import request

def ip_range(debut, fin):
    x1, x2, x3, x4 = [int(x) for x in debut.split('.')]
    y1, y2, y3, y4 = [int(y) for y in fin.split('.')]
    ip_list = list()
    while True:
        if [x1, x2, x3, x4] == [y1, y2, y3, y4]:
            break
        ip_list.append('%d.%d.%d.%d' % (x1, x2, x3, x4))
        if x4 >= 255 or x4 == 0:
            x4 = 1
            if x3 >= 255 or x3 == 0:
                x3 = 1
                if x2 >= 255 or x2 == 0:
                    x2 = 1
                    x1 += 1
                else:
                    x2 += 1
            else:
                x3 += 1
        else:
            x4 += 1
    return ip_list


ips = ip_range("41.87.128.1", "41.87.159.255")

ports = range(80, 9999)

for ip in ips:
    for port in ports:
        url = 'http://%s:%s' % (ip, port)
        print('Essai %s' % url)
        try:
            with request.urlopen(url, None, 30) as r:
                print('OK', r.status, r.reason)
        except Exception as e:
            # print('Echec %s %s' % (url, e))
