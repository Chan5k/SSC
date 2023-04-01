import subprocess

def improve_internet_speed(interface):
    # enable TCP window scaling
    subprocess.run(["sudo", "sysctl", "-w", "net.ipv4.tcp_window_scaling=1"])
    subprocess.run(["sudo", "sysctl", "-w", "net.ipv4.tcp_timestamps=1"])

    # set the receive socket buffer size
    subprocess.run(["sudo", "sysctl", "-w", f"net.core.rmem_max=16777216"])
    subprocess.run(["sudo", "sysctl", "-w", f"net.core.rmem_default=31457280"])

    # set the send socket buffer size
    subprocess.run(["sudo", "sysctl", "-w", f"net.core.wmem_max=16777216"])
    subprocess.run(["sudo", "sysctl", "-w", f"net.core.wmem_default=31457280"])

    # set the TCP buffer size
    subprocess.run(["sudo", "sysctl", "-w", f"net.ipv4.tcp_rmem=4096 87380 {31457280*2}"])
    subprocess.run(["sudo", "sysctl", "-w", f"net.ipv4.tcp_wmem=4096 65536 {31457280*2}"])

    # set the congestion control algorithm to BBR
    subprocess.run(["sudo", "sysctl", "-w", f"net.ipv4.tcp_congestion_control=bbr"])

    print("Internet speed has been improved!")
