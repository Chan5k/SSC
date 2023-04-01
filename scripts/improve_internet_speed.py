import os
import sys
import subprocess

def improve_internet_speed(interface):
    print("This will make changes to your system's network settings. Do you wish to continue? (y/n)")
    confirmation = input("> ")

    if confirmation.lower() != "y":
        print("Aborting.")
        sys.exit()

    print("Improving internet speed...")

    # Disable IPv6
    subprocess.run(["sudo", "sysctl", "-w", "net.ipv6.conf.all.disable_ipv6=1"])
    subprocess.run(["sudo", "sysctl", "-w", "net.ipv6.conf.default.disable_ipv6=1"])

    # Enable TCP Fast Open
    subprocess.run(["sudo", "sysctl", "-w", "net.ipv4.tcp_fastopen=3"])

    # Enable TCP congestion control BBR
    subprocess.run(["sudo", "modprobe", "tcp_bbr"])
    subprocess.run(["sudo", "sysctl", "-w", "net.core.default_qdisc=fq"])
    subprocess.run(["sudo", "sysctl", "-w", "net.ipv4.tcp_congestion_control=bbr"])

    # Prompt the user to choose a DNS server
    print("Which DNS server do you want to use? Enter the corresponding number:")
    print("1. Google DNS (8.8.8.8, 8.8.4.4)")
    print("2. Cloudflare DNS (1.1.1.1, 1.0.0.1)")
    dns_selection = input("> ")

    # Set DNS servers based on user's choice
    if dns_selection == "1":
        subprocess.run(["sudo", "systemd-resolve", "--set-dns", "8.8.8.8", "--interface", interface])
        subprocess.run(["sudo", "systemd-resolve", "--set-dns", "8.8.4.4", "--interface", interface])
        print("DNS servers set to Google DNS (8.8.8.8, 8.8.4.4)")
    elif dns_selection == "2":
        subprocess.run(["sudo", "systemd-resolve", "--set-dns", "1.1.1.1", "--interface", interface])
        subprocess.run(["sudo", "systemd-resolve", "--set-dns", "1.0.0.1", "--interface", interface])
        print("DNS servers set to Cloudflare DNS (1.1.1.1, 1.0.0.1)")
    else:
        print("Invalid selection.")
        sys.exit(1)

    print("Done.")

if __name__ == "__main__":
    interface = input("Enter the name of your network interface: ")
    improve_internet_speed(interface)