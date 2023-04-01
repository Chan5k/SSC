import os

def change_dns_servers(dns_servers):
    # remove the existing nameserver entries from /etc/resolvconf/resolv.conf.d/head
    os.system("sudo sed -i '/nameserver/d' /etc/resolvconf/resolv.conf.d/head")

    # write the new nameserver entries to /etc/resolvconf/resolv.conf.d/head
    with open("/etc/resolvconf/resolv.conf.d/head", "a") as f:
        f.write("\n".join(["nameserver " + dns_server for dns_server in dns_servers]) + "\n")

    # remove the existing nameserver entries from /etc/resolv.conf
    os.system("sudo sed -i '/nameserver/d' /etc/resolv.conf")

    # write the new nameserver entries to /etc/resolv.conf
    with open("/etc/resolv.conf", "a") as f:
        f.write("\n".join(["nameserver " + dns_server for dns_server in dns_servers]) + "\n")

    # update resolvconf to use the new nameserver entries
    os.system("sudo resolvconf -u")
