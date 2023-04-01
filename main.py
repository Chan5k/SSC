import os
import sys
sys.path.append("scripts")

from internet import test_internet_speed
from cpu import test_cpu_stress, get_cpu_score
from disk import test_disk_speed
from security import test_security
from firewall import improve_firewall_rules
from change_dns_servers import change_dns_servers
from improve_internet_speed import improve_internet_speed

def main():
    while True:
        # ask the user what test they want to run
        print("What would you like to do? Enter the corresponding number:")
        print("1. Test internet speed")
        print("2. Test CPU stress")
        print("3. Test disk speed")
        print("4. Test security (Don't use this on a production server!)")
        print("5. Improve firewall rules")
        print("6. Improve internet speed")
        print("7. Change DNS servers")
        print("8. Exit")
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
        elif selection == "6":
            interface = input("Enter the name of your network interface (e.g. eth0): ")
            improve_internet_speed(interface)
        elif selection == "7":
            dns_server = input("Enter the new DNS server (e.g. 1.1.1.1): ")
            change_dns_servers(dns_server)
        elif selection == "8":
            sys.exit()

        # ask the user if they want to return to the main menu or exit
        print()
        choice = input("Press Enter to return to the main menu or type 'exit' to quit: ")
        print()

        # clear the screen if the user chooses to return to the main menu
        if choice == "" or choice.lower() == "exit":
            if os.name == "nt":
                os.system("cls")
            else:
                os.system("clear")
        else:
            sys.exit()

if __name__ == "__main__":
    main()
