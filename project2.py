#  Zion Needham (Ultimate-Shoe)
#  W25 COP2002.0M1.
#  04/19/2025
#  Port Protocols Study Program
#  Simple Python program to assist IT students studying port numbers and protocols

import random # To be able to pull random options from our dictionary for creating questions.

def main_menu():
    """Outputs the main menu options."""

    print("Main Menu:")
    print("1. Given a port number, identify the PROTOCOL (use abbreviation).")
    print("2. Given a port protocol, identify a port NUMBER.")
    print("3. Exit")

def identify_protocol(port_to_protocols_dict):
    ''' Handle studying for option 1 - identify the protocol for a given port number.'''

    # Print header info for Option 1
    print("Option 1: Identify the port's PROTOCOL.")
    print("---------------------------------------\n")

    # Variable for loop
    done = False

    # Allow user to keep studying by asking questions until they're done.
    while not done:
        # Prepare the practice question by pulling a random port number protocol and save the correct protocol
        random_Port = random.choice(list(port_to_protocols_dict.keys()))
        correct_Protocol = port_to_protocols_dict[random_Port].upper()

        # Force user to enter the loop
        userProtocol_Answer = ""

        # Keep reprompting the question when user hits Enter (inputs no choice)
        while userProtocol_Answer == "":
            userProtocol_Answer = input(f"What is the protocol for port {random_Port} (m=Main Menu)? ").upper() # Ask the question; user answer is uppercase

        # Determine whether user answered or is done.
        if userProtocol_Answer == "M":  # End the loop and return to main menu
            done = True
        else:   # User answered
  
            # Check if user's answer is the correct protocol (correct answer needs to be uppercase for the comparison)
            if userProtocol_Answer == correct_Protocol.upper():
                print("Correct answer!\n")
            else:
                print(f"Incorrect. The correct answer is {correct_Protocol}.\n")


def identify_port(protocol_to_ports):
    ''' Handle studying for option 2 - identify the port number for a given protocol.'''

    # Print header info for Option 2
    print("Option 2: Identify the port's NUMBER.")
    print("---------------------------------------\n")
    
    # Variable for loop
    done = False

    # Allow user to keep studying by asking questions until they're done.
    while not done:
        # Prepare the practice question by pulling a random port protocol and save the correct port
        random_Protocol = random.choice(list(protocol_to_ports.keys()))
        correct_Ports = protocol_to_ports[random_Protocol]

        # Force to enter the loop
        userPortnum_Answer = ""

        # Keep reprompting the question when user hits Enter (inputs no choice)
        while userPortnum_Answer == "":
            userPortnum_Answer = input(f"What is the number for protocol {random_Protocol} (m=Main Menu)? ").upper() # Ask the question; user answer is uppercase

        # Determine whether user answered or is done.
        if userPortnum_Answer == "M":  # End the loop and return to main menu
            done = True
        else:   # User answered
            
            # Check if user's answer is the correct port number
            if userPortnum_Answer in correct_Ports:
                print("Correct answer!\n")
            else:
                # We manually create a comma-separated answer list (if more than one correct answer)
                answer_line = ""
                for i in range(len(correct_Ports)):
                    answer_line += correct_Ports[i]
                    if i < len(correct_Ports) - 1:  # If we have more than one correct answer in the list
                        answer_line += " or " # Tell user both answers that are correct

                print(f"Incorrect. The correct answer is {answer_line}.\n")

def main():
    # Variable for knowing when user is finished with the loop
    done = False

    # Dictionary to map port numbers and their corresponding port protocols
    port_to_protocols_dict = {
    "20": "FTP",
    "21": "FTP",
    "22": "SSH",
    "23": "Telnet",
    "25": "SMTP",
    "53": "DNS",
    "67": "DHCP",
    "68": "DHCP",
    "80": "HTTP",
    "110": "POP3",
    "137": "NetBIOS",
    "139": "NetBIOS",
    "143": "IMAP",
    "161": "SNMP",
    "162": "SNMP",
    "389": "LDAP",
    "443": "HTTPS",
    "445": "SMB",
    "3389": "RDP",
    }
    
    # Reverse dictionary for checking pairs with multiple correct answers; ie. FTP, NetBIOS, SNMP
    protocol_to_ports = {}  # We start with an empty list
    for port, protocol in port_to_protocols_dict.items():

        # We add those protocols that are not yet in the list
        if protocol not in protocol_to_ports:   
            protocol_to_ports[protocol] = [port]
        else:
            protocol_to_ports[protocol].append(port)

    # Allow user to keep studying until finished
    while(not done):
            # Bring user to the main menu screen
        main_menu()

        # Get the user's choice
        user_choice = input("\nChoice: ")

        while user_choice not in ["1", "2", "3"]:
            user_choice = input("Invalid. Enter choice: ")
        
        # Do the option associated with the user's choice
        if(user_choice == "1"): # Option 1
            identify_protocol(port_to_protocols_dict)
            print() # Blank Spacing
        elif(user_choice == "2"): # Option 2
            identify_port(protocol_to_ports)
            print()
        else: # User wants to quit
            done = True
            print()

        # Ending output message
    print("Program Complete. I hope this has helped in studying for the CompTIA A+ Certification.")

if( __name__=="__main__"):
    main()
