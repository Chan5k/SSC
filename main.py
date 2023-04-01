import platform
import sys

if platform.system() != "Linux":
    print("This script is only compatible with Linux systems.")
    sys.exit(1)

sys.path.append("scripts")

from cpu import test_cpu_stress, get_cpu_score
from disk import test_disk_speed
from firewall import improve_firewall_rules
from internet import test_internet_speed
from security import test_security

def main():
    # ask the user what test they want to run
    print("What would you like to do? Enter the corresponding number:")
    print("1. Test internet speed")
    print("2. Test CPU stress")
    print("3. Test disk speed")
    print("4. Test security")
    print("5. Improve firewall rules")
    selection = input("> ")

    # execute the selected option
    if selection == "1":
        test_internet_speed()
    elif selection == "2":
        duration = int(input("Enter the duration of the CPU stress test (in seconds): "))
        test_cpu_stress(duration)
        score = get_cpu_score()
        print(f"CPU score: {score}")
    elif selection == "3":
        test_disk_speed()
    elif selection == "4":
        test_security()
    elif selection == "5":
        improve_firewall_rules()
    else:
        print("Invalid selection.")
        sys.exit(1)

if __name__ == "__main__":
    main()
