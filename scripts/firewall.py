import subprocess

def improve_firewall_rules():
    print("Improving firewall rules...")
    # allow ssh connections from trusted IP addresses
    ssh_ips = ["192.168.0.1", "192.168.0.2"]
    for ip in ssh_ips:
        cmd = f"sudo ufw allow from {ip} to any port 22"
        subprocess.run(cmd, shell=True)
    # allow HTTP and HTTPS traffic
    cmd = "sudo ufw allow http"
    subprocess.run(cmd, shell=True)
    cmd = "sudo ufw allow https"
    subprocess.run(cmd, shell=True)
    # enable UFW firewall
    cmd = "sudo ufw enable"
    subprocess.run(cmd, shell=True)
