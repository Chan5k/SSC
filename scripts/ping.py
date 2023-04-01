import subprocess

def ping_host(host):
    # Run the ping command and capture the output
    try:
        output = subprocess.check_output(["ping", "-c", "5", host], universal_newlines=True)
    except subprocess.CalledProcessError:
        return f"Unable to ping host {host}"
    
    # Parse the output to extract relevant information
    lines = output.strip().split("\n")
    if len(lines) < 2:
        return f"Unable to ping host {host}"
    stats = lines[-1].split(", ")
    packet_loss = stats[2].split()[0]
    min_time, avg_time, max_time, mdev = [time.split()[1] for time in stats[3:]]
    
    # Return a formatted string with the ping results
    return f"Ping statistics for {host}:\n\tPacket Loss = {packet_loss}\n\tMinimum Time = {min_time}\n\tAverage Time = {avg_time}\n\tMaximum Time = {max_time}\n\tStandard Deviation = {mdev}"
