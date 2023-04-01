import subprocess

def improve_internet_speed():
    print("This feature will change your DNS servers to Cloudflare or Google DNS servers.")
    print("Please choose an option:")
    print("1. Cloudflare")
    print("2. Google")
    choice = input("> ")
    if choice == "1":
        subprocess.run(["sudo", "sed", "-i", "s/nameserver.*/nameserver 1.1.1.2\nnameserver 1.0.0.2/g", "/etc/resolv.conf"])
        print("DNS servers updated to Cloudflare.")
    elif choice == "2":
        subprocess.run(["sudo", "sed", "-i", "s/nameserver.*/nameserver 8.8.8.8\nnameserver 8.8.4.4/g", "/etc/resolv.conf"])
        print("DNS servers updated to Google.")
    else:
        print("Invalid selection.")
