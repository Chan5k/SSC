import subprocess

def improve_internet_speed():
    # Ask user to choose between Cloudflare and Google DNS
    while True:
        dns_choice = input("Choose your DNS provider ('1' for Cloudflare, '2' for Google): ")
        if dns_choice == '1':
            dns1 = '1.1.1.2'
            dns2 = '1.0.0.2'
            break
        elif dns_choice == '2':
            dns1 = '8.8.8.8'
            dns2 = '8.8.4.4'
            break
        else:
            print("Invalid choice. Please choose either '1' or '2'.")

    # Edit the /etc/resolv.conf file to use the chosen DNS servers
    try:
        with open('/etc/resolv.conf', 'w') as f:
            f.write(f'nameserver {dns1}\n')
            f.write(f'nameserver {dns2}\n')
            print(f'Successfully changed DNS servers to {dns1} and {dns2}.')
    except Exception as e:
        print(f'Error changing DNS servers: {e}')
