import subprocess

def improve_firewall_rules():
    """
    Improve UFW firewall rules to enhance system security.
    """
    print("Improving firewall rules...")
    subprocess.run(["sudo", "ufw", "default", "deny", "incoming"])
    subprocess.run(["sudo", "ufw", "default", "allow", "outgoing"])
    subprocess.run(["sudo", "ufw", "allow", "ssh"])
    subprocess.run(["sudo", "ufw", "allow", "http"])
    subprocess.run(["sudo", "ufw", "allow", "https"])
    subprocess.run(["sudo", "ufw", "allow", "53"])
    subprocess.run(["sudo", "ufw", "allow", "123/udp"])
    subprocess.run(["sudo", "ufw", "allow", "5060/udp"])
    subprocess.run(["sudo", "ufw", "allow", "5060/tcp"])
    subprocess.run(["sudo", "ufw", "allow", "5190/tcp"])
    subprocess.run(["sudo", "ufw", "allow", "5222/tcp"])
    subprocess.run(["sudo", "ufw", "allow", "5223/tcp"])
    subprocess.run(["sudo", "ufw", "allow", "5280/tcp"])
    subprocess.run(["sudo", "ufw", "allow", "8443/tcp"])
    subprocess.run(["sudo", "ufw", "allow", "8080/tcp"])
    subprocess.run(["sudo", "ufw", "allow", "5672/tcp"])
    subprocess.run(["sudo", "ufw", "allow", "27017/tcp"])
    subprocess.run(["sudo", "ufw", "allow", "6379/tcp"])
    subprocess.run(["sudo", "ufw", "allow", "9418/tcp"])
    subprocess.run(["sudo", "ufw", "allow", "9418/udp"])
    subprocess.run(["sudo", "ufw", "allow", "33434:33523/udp"])
    subprocess.run(["sudo", "ufw", "allow", "33434:33523/tcp"])
    print("Firewall rules updated.")
