import sys
from scripts.internet_speed_test import test_internet_speed
from scripts.cpu_stress_test import test_cpu_stress
from scripts.disk_speed_test import test_disk_speed

def main():
    # ask the user what test they want to run
    print("Which test would you like to run? Enter the corresponding number:")
    print("1. Internet speed test")
    print("2. CPU stress test")
    print("3. Disk speed test")
    selection = input("> ")

    # execute the selected test
    if selection == "1":
        test_internet_speed()
    elif selection == "2":
        duration = int(input("Enter the duration of the CPU stress test (in seconds): "))
        test_cpu_stress(duration)
    elif selection == "3":
        test_disk_speed()
    else:
        print("Invalid selection.")
        sys.exit(1)

if __name__ == "__main__":
    main()
