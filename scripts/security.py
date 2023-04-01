import os
import subprocess

def test_security():
    """
    Runs a security check on the system to detect malware and other security issues.
    """
    # Check for malware
    print("Malware scan started, please wait")
    output = subprocess.check_output(["sudo", "clamscan", "-r", "/"])

    # Display the results
    print(output.decode("utf-8"))

    # Check for open ports
    print("Checking open ports")
    output = subprocess.check_output(["sudo", "netstat", "-tulpn"])

    # Display the results
    print(output.decode("utf-8"))