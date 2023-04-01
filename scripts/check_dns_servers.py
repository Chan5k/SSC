import os

def check_dns_servers():
    with open('/etc/resolv.conf', 'r') as f:
        lines = f.readlines()
    
    # Extract the nameservers from resolv.conf
    nameservers = []
    for line in lines:
        if line.startswith('nameserver'):
            nameservers.append(line.split()[1])
    
    # Print the nameservers
    if len(nameservers) == 0:
        print('No nameservers found in /etc/resolv.conf')
    else:
        print('DNS servers:')
        for nameserver in nameservers:
            print(nameserver)
