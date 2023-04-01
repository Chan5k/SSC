import subprocess

def improve_internet_speed():
    # Ask the user which DNS provider to use
    dns_provider = input("Which DNS provider do you want to use? (1 for Cloudflare, 2 for Google): ")
    while dns_provider not in ["1", "2"]:
        dns_provider = input("Invalid input. Please enter 1 for Cloudflare or 2 for Google: ")

    if dns_provider == "1":
        # Use Cloudflare DNS
        nameservers = ["1.1.1.2", "1.0.0.2"]
    elif dns_provider == "2":
        # Use Google DNS
        nameservers = ["8.8.8.8", "8.8.4.4"]

    # Create the new resolv.conf contents
    new_resolv_conf = "\n".join(["nameserver " + ns for ns in nameservers])

    # Write the new resolv.conf contents to a temporary file
    with open("/tmp/new_resolv_conf", "w") as f:
        f.write(new_resolv_conf)

    # Replace the current resolv.conf with the new one
    subprocess.run(["sudo", "mv", "/tmp/new_resolv_conf", "/etc/resolv.conf"])
    
    print("DNS servers have been updated to", ", ".join(nameservers))
