import netifaces as ni

def show_interfaces():
    interfaces = ni.interfaces()
    print('{:<10} {:<15}'.format('Interface', 'IPv4 Address'))
    print('-' * 30)
    for iface in interfaces:
        try:
            ip = ni.ifaddresses(iface)[ni.AF_INET][0]['addr']
        except:
            ip = 'N/A'
        print('{:<10} {:<15}'.format(iface, ip))
