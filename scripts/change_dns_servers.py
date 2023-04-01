import subprocess

def change_dns_servers():
    print("Which DNS servers would you like to use?")
    print("1. Cloudflare (1.1.1.1, 1.0.0.1)")
    print("2. Google (8.8.8.8, 8.8.4.4)")
    selection = input("> ")

    if selection == "1":
        nameservers = ["1.1.1.1", "1.0.0.1"]
    elif selection == "2":
        nameservers = ["8.8.8.8", "8.8.4.4"]
    else:
        print("Invalid selection.")
        return

    # Remove old nameservers from /etc/resolv.conf
    subprocess.run(["sudo", "sed", "-i", "/nameserver/d", "/etc/resolv.conf"])

    # Remove old nameservers from /etc/resolvconf/resolv.conf.d/head
    subprocess.run(["sudo", "sed", "-i", "/nameserver/d", "/etc/resolvconf/resolv.conf.d/head"])

    # Add new nameservers to /etc/resolv.conf and /etc/resolvconf/resolv.conf.d/head
    with open("/etc/resolv.conf", "a") as f:
        for nameserver in nameservers:
            f.write("nameserver {}\n".format(nameserver))
    with open("/etc/resolvconf/resolv.conf.d/head", "a") as f:
        for nameserver in nameservers:
            f.write("nameserver {}\n".format(nameserver))

    # Restart the resolvconf service to apply the changes
    subprocess.run(["sudo", "systemctl", "restart", "resolvconf"])
    print("DNS servers updated successfully.")
