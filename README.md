# Sys-Speed-Check
Sys-Speed-Check is a Linux-based command-line tool that checks the speed of disk, CPU, and internet connection on Ubuntu and Debian-based systems. It uses hdparm, lscpu, and speedtest-cli to provide quick feedback on system performance.

# Features

    - Internet speed test
    - CPU Performance test
    - Disk speed test

The script uses separate files for each test, and requires the following Python packages to be installed:
    
    - `speedtest-cli`
    - `psutil`
    - `py-cpuinfo`

# Installation
To install the required Python packages, run the following command:

```bash
pip3 install -r requirements.txt
```
This will install the required packages listed in the requirements.txt file.

# Usage

To run the script, execute the `main.py` file using Python:

```bash
python3 main.py
```
This will display a menu of options for running the different tests. Select an option by entering the corresponding number.

# Internet speed test
The internet speed test uses the `speedtest-cli` package to measure the download and upload speed of your internet connection.
# CPU stress test
The CPU stress test uses the `psutil` package to run a stress test on your CPU for a specified duration, and then calculates a CPU score based on the average CPU usage during the test.
# Disk speed test
The disk speed test measures the read and write speed of your disk by reading and writing a large file.
# License
This script is licensed under the MIT License. See the LICENSE file for more information.
