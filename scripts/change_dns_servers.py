import os


def change_dns_servers():
    """
    Changes the DNS servers to Cloudflare or Google.
    """
    print("Choose the DNS server you want to use:")
    print("1. Cloudflare (1.1.1.2, 1.0.0.2)")
    print("2. Google (8.8.8.8, 8.8.4.4)")
    selection = input("> ")
    if selection == "1":
        nameservers = ["nameserver 1.1.1.2", "nameserver 1.0.0.2"]
    elif selection == "2":
        nameservers = ["nameserver 8.8.8.8", "nameserver 8.8.4.4"]
    else:
        print("Invalid selection.")
        return

    # Change /etc/resolv.conf
    with open("/etc/resolv.conf", "w") as f:
        f.write("\n".join(nameservers))

    # Change /etc/resolvconf/resolv.conf.d/head
    with open("/etc/resolvconf/resolv.conf.d/head", "w") as f:
        f.write("\n".join(nameservers))

    # Update resolv.conf
    os.system("resolvconf -u")

    print("DNS servers updated successfully.")
