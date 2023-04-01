import subprocess

def improve_internet_speed(interface):
    # disable IPv6
    subprocess.run(["sudo", "sysctl", "-w", f"net.ipv6.conf.{interface}.disable_ipv6=1"])

    # enable TCP BBR congestion control
    subprocess.run(["sudo", "modprobe", "tcp_bbr"])
    with open("/etc/sysctl.conf", "a") as file:
        file.write("\n# Enable TCP BBR congestion control\n")
        file.write("net.core.default_qdisc=fq\n")
        file.write(f"net.ipv4.tcp_congestion_control=bbr\n")

    # set the MTU to 9000
    subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "mtu", "9000"])

    # restart the network interface
    subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "down"])
    subprocess.run(["sudo", "ip", "link", "set", "dev", interface, "up"])
    
    print("Internet speed improved!")
