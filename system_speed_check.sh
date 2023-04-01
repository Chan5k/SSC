#!/bin/bash

# Display welcome message and options
echo "Hello and welcome to SysSpeedCheck. Please select an option for your desired benchmark:"
echo "  1. Disk speed test"
echo "  2. CPU speed test"
echo "  3. CPU benchmark"
echo "  4. Internet speed test"

# Read user input
read -p "Enter option number: " option

# Check if the script is run on Ubuntu or Debian
if ! (grep -q -E "Ubuntu|Debian" /etc/os-release); then
    echo "This script is intended for use on Ubuntu or Debian-based systems only. Exiting."
    exit 1
fi

# Install required packages if not already installed
if ! (command -v hdparm > /dev/null) || ! (command -v speedtest-cli > /dev/null) || ! (command -v sysbench > /dev/null); then
    echo "Installing required packages..."
    sudo apt update
    sudo apt install hdparm speedtest-cli sysbench -y
fi

# Check disk speed
if [ "$option" == "1" ]; then
    echo "Checking disk speed..."
    disk=$(df / | tail -1 | awk '{print $1}')
    sudo hdparm -Tt "$disk"

# Check CPU speed
elif [ "$option" == "2" ]; then
    echo "Checking CPU speed..."
    echo "Model name: $(lscpu | grep "Model name" | awk '{$1=""; print $0}')"
    echo "CPU cores:"
    lscpu | grep "CPU MHz" | awk '{print "  Core "$1": "$4" MHz"}'
    lscpu | grep "CPU max MHz" | awk '{print "  Max frequency: "$4" MHz"}'

# Run CPU benchmark
elif [ "$option" == "3" ]; then
    echo "Running CPU benchmark..."
    cpu_score=$(sysbench cpu --time=30 --threads=0 --events=0 --cpu-max-prime=20000 run | grep "total time:" | awk '{print $3}' | cut -d '.' -f 1)
    cpu_score=$((200000/$cpu_score))
    echo "CPU score: $cpu_score/100"
    if [ "$cpu_score" -ge 70 ]; then
        echo "CPU performance is good."
    else
        echo "CPU performance is poor."
    fi

# Check internet speed
elif [ "$option" == "4" ]; then
    echo "Checking internet speed..."
    speedtest-cli
else
    echo "Invalid option. Exiting."
    exit 1
fi

echo "All tests completed."
