import socket
def check_dns_servers():
    # Open the resolv.conf file
    with open('/etc/resolv.conf', 'r') as f:
        lines = f.readlines()
    
    # Get the nameservers from the file
    nameservers = []
    for line in lines:
        if line.startswith('nameserver'):
            parts = line.split()
            if len(parts) >= 2:
                nameservers.append(parts[1])

    # Check if the nameservers are valid
    valid_nameservers = []
    for ns in nameservers:
        try:
            socket.inet_aton(ns)
            valid_nameservers.append(ns)
        except socket.error:
            pass

    # Print the valid nameservers
    print('DNS Servers:')
    if len(valid_nameservers) == 0:
        print('No valid nameservers found.')
    else:
        for ns in valid_nameservers:
            print(ns)
