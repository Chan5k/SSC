import os
import sys
sys.path.append("scripts")

from internet import test_internet_speed
from cpu import test_cpu_stress, get_cpu_score
from disk import test_disk_speed
from security import test_security
from firewall import improve_firewall_rules

def main():
    while True:
        # ask the user what test they want to run
        print("What would you like to do? Enter the corresponding number:")
        print("1. Test internet speed")
        print("2. Test CPU stress")
        print("3. Test disk speed")
        print("4. Test security")
        print("5. Improve firewall rules")
        print("6. Exit")
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

        # ask the user if they want to return to the main menu or exit
        print()
        choice = input("Press Enter to return to the main menu or type 'exit' to quit: ")
        print()

        # clear the screen if the user chooses to return to the main menu
        if choice == "":
            os.system('cls' if os.name=='nt' else 'clear')
        else:
            sys.exit()

if __name__ == "__main__":
    main()
