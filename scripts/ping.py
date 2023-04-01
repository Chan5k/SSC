import subprocess

def ping(host):
    # Run the ping command and capture the output
    try:
        output = subprocess.check_output(["ping", "-c", "5", host], universal_newlines=True)
    except subprocess.CalledProcessError:
        return f"Unable to ping host {host}"

    # Parse the output to extract relevant information
    lines = output.strip().split("\n")
    rtt_stats = lines[-1].split()[3].split("/")
    packet_loss = lines[-2].split(",")[2].split()[0]

    # Return a formatted string with the ping results
    return f"Ping statistics for {host}:\n\tPacket Loss = {packet_loss}%\n\tMinimum Time = {rtt_stats[0]} ms\n\tAverage Time = {rtt_stats[1]} ms\n\tMaximum Time = {rtt_stats[2]} ms\n\tStandard Deviation = {rtt_stats[3]} ms"
