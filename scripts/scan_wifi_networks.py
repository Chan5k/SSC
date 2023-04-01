import subprocess

def scan_wifi_networks():
    # run nmap to scan for wifi networks
    cmd_output = subprocess.check_output(['sudo', 'nmap', '-sP', '-oG', '-','192.168.1.1/24'], universal_newlines=True)

    # parse the output of nmap and extract the wifi networks
    networks = []
    for line in cmd_output.split('\n'):
        if 'Host:' in line:
            fields = line.strip().split()
            ip_address = fields[1]
            hostname = fields[2].strip('()')
            if hostname.startswith('WLAN_'):
                networks.append({'ssid': hostname[5:], 'ip_address': ip_address})

    # print the available wifi networks
    if len(networks) == 0:
        print('No wifi networks found.')
    else:
        print('{:<20} {}'.format('SSID', 'IP Address'))
        print('-' * 30)
        for network in networks:
            print('{:<20} {}'.format(network['ssid'], network['ip_address']))
