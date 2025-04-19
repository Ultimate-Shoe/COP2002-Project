#  Zion Needham (Ultimate-Shoe)
#  W25 COP2002.0M1.
#  04/18/2025
#  Port Protocols Study Program
#  Simple Python program to assist IT students studying port numbers and protocols

import random # To be able to pull random options from our dictionary for creating questions.

def main_menu():
    """Outputs the main menu options."""

    print("Main Menu:")
    print("1. Given a port number, identify the PROTOCOL (use abbreviation).")
    print("2. Given a port protocol, identify a port NUMBER.")
    print("3. Exit")

def getUserChoice():
    ''' Get the user's choice from the main menu ensuring it is either 1, 2, or 3.'''

    userChoice = input("\nChoice: ")

    while userChoice not in ["1", "2", "3"]:
        userChoice = input("Invalid. Enter choice: ")
        
    return userChoice

def get_RandomPort(port_dict):
    ''' Picks a random port number from our list of ports to use in our practice questions.'''
    
    random_portnum_key = random.choice(tuple(port_dict.keys()))
    return random_portnum_key

def get_RandomProtocol(port_dict):
    ''' Picks a random protocol from our list of protocols to use in our practice questions..'''

    random_porotocol_value = random.choice(tuple(port_dict.values()))
    return random_porotocol_value

def whatProtocol(inputPort, port_dict):
    ''' Matches and converts a given port number to it's corresponding protocol.'''

    return port_dict.get(inputPort)

def reverse_port_dict(port_dict):
    ''' Creates a reverse dictionary that maps port numbers and protocols to a list. '''

    protocol_to_ports = {}  # We start with an empty list
    for port, protocol in port_dict.items():
        protocol = protocol.upper()

        # We add those protocols that are not yet in the list
        if protocol not in protocol_to_ports:   
            protocol_to_ports[protocol] = [port]
        else:
            protocol_to_ports[protocol].append(port)

    return protocol_to_ports

def option1(port_dict):
    ''' Handle studying for option 1 - identify the protocol for a given port number.'''

    # Print header info for Option 1
    print("Option 1: Identify the port's PROTOCOL.")
    print("---------------------------------------\n")

    # Variable for loop
    done = False

    # Allow user to keep studying by asking questions until they're done.
    while not done:
        # Randomize a port number for our practice question.
        randomPort = get_RandomPort(port_dict)

        # Force user to enter the loop
        userAnswer = ""

        # Keep reprompting the question when user hits Enter (inputs no choice)
        while userAnswer == "":
            userAnswer = input(f"What is the protocol for port {randomPort} (m=Main Menu)? ").upper() # Ask the question; user answer is uppercase

        # Determine whether user answered or is done.
        if userAnswer == "M":  # End the loop and return to main menu
            done = True
        else:   # User answered
            # Calculate the correct answer protocol
            correctProtocol = whatProtocol(randomPort, port_dict)

            # Check if user's answer is the correct protocol (correct answer needs to be uppercase for the comparison)
            if userAnswer == correctProtocol.upper():
                print("Correct answer!\n")
            else:
                print(f"Incorrect. The correct answer is {correctProtocol}.\n")


def option2(port_dict, protocol_to_ports):
    ''' Handle studying for option 2 - identify the port number for a given protocol.'''

    # Print header info for Option 2
    print("Option 2: Identify the port's NUMBER.")
    print("---------------------------------------\n")
    
    # Variable for loop
    done = False

    # Allow user to keep studying by asking questions until they're done.
    while not done:
        # Prepare the practice question by pulling a random port protocol
        randomProtocol = get_RandomProtocol(port_dict)

        # Force to enter the loop
        userPortnum_Answer = ""

        # Keep reprompting the question when user hits Enter
        while userPortnum_Answer == "":
            userPortnum_Answer = input(f"What is the number for protocol {randomProtocol}(m=Main Menu)? ").upper() # Ask the question; user answer is uppercase

        # Determine whether user answered or is done.
        if userPortnum_Answer == "M":  # End the loop and return to main menu
            done = True
        else:   # User answered
            correct_ports = protocol_to_ports.get(randomProtocol.upper(), [])

            # Check if user's answer is the correct port number
            if userPortnum_Answer in correct_ports:
                print("Correct answer!\n")
            else:
                # We manually create a comma-separated list
                answer_line = ""
                for i in range(len(correct_ports)):
                    answer_line += correct_ports[i]
                    if i < len(correct_ports) - 1:  # If we have multiple correct answers
                        answer_line += ", "

                print(f"Incorrect. The correct answer is {answer_line}.\n")

def main():
    # Variable for knowing when user is finished with the loop
    done = False

    # Dictionary to map port numbers and their corresponding port protocols
    port_dict = {
        "20": "FTP", "21": "FTP", "22": "SSH", "23": "Telnet", "25": "SMTP",
        "53": "DNS", "67": "DHCP", "68": "DHCP", "80": "HTTP", "110": "POP3",
        "137": "NetBIOS", "139": "NetBIOS", "143": "IMAP", "161": "SNMP",
        "162": "SNMP", "389": "LDAP", "443": "HTTPS", "445": "SMB", "3389": "RDP"
    }
    
    # Reverse dictionary for checking pairs with multiple correct answers; ie. FTP, NetBIOS, SNMP
    protocol_to_ports = reverse_port_dict(port_dict)

    # Allow user to keep studying until finished
    while(not done):
            # Bring user to the main menu screen
        main_menu()

        # Get the user's choice
        choice = getUserChoice()
        
        # Do the option associated with the user's choice
        if(choice == "1"): # Option 1
            option1(port_dict)
            print() # Blank Spacing
        elif(choice == "2"): # Option 2
            option2(port_dict, protocol_to_ports)
            print()
        else: # User wants to quit
            done = True
            print()

        # Ending output message
    print("Program Complete. I hope this has helped in studying for the CompTIA A+ Certification.")

if( __name__=="__main__"):
    main()