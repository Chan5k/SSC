import subprocess

def scan_wifi_networks():
    """
    Scans for available WiFi networks and returns a list of networks with their details.
    """
    # Run the iwlist command to scan for available WiFi networks
    cmd_output = subprocess.check_output(['iwlist', 'wlan0', 'scan'], universal_newlines=True)

    # Split the output into a list of lines
    lines = cmd_output.split('\n')

    # Create a list to hold the available networks
    networks = []

    # Loop through the lines and extract the network details
    for line in lines:
        if 'ESSID' in line:
            ssid = line.split(':')[1].strip().strip('"')
        elif 'Quality' in line:
            quality = line.split('=')[1].split()[0]
        elif 'Encryption key' in line:
            encryption = line.split(':')[1].strip()
        elif 'Frequency:' in line:
            freq = line.split()[3].split(':')[1]
        elif 'Mode:' in line:
            mode = line.split(':')[1].strip()
        elif 'Address:' in line:
            address = line.split()[4]
        elif 'Channel' in line:
            channel = line.split(':')[1]

            # Append the network to the list
            networks.append({
                'ssid': ssid,
                'quality': quality,
                'encryption': encryption,
                'freq': freq,
                'mode': mode,
                'address': address,
                'channel': channel
            })

    # Return the list of available networks
    return networks
