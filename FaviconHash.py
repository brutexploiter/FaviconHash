import mmh3
import requests
import codecs
import os
import sys
import random
from termcolor import colored

def logo():
    banner = colored('''
$$$$$$$$\                 $$\                               $$\   $$\                     $$\       
$$  _____|                \__|                              $$ |  $$ |                    $$ |      
$$ |   $$$$$$\ $$\    $$\ $$\  $$$$$$$\  $$$$$$\  $$$$$$$\  $$ |  $$ | $$$$$$\   $$$$$$$\ $$$$$$$\  
$$$$$\ \____$$\\$$\  $$  |$$ |$$  _____|$$  __$$\ $$  __$$\ $$$$$$$$ | \____$$\ $$  _____|$$  __$$\ 
$$  __|$$$$$$$ |\$$\$$  / $$ |$$ /      $$ /  $$ |$$ |  $$ |$$  __$$ | $$$$$$$ |\$$$$$$\  $$ |  $$ |
$$ |  $$  __$$ | \$$$  /  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$  __$$ | \____$$\ $$ |  $$ |
$$ |  \$$$$$$$ |  \$  /   $$ |\$$$$$$$\ \$$$$$$  |$$ |  $$ |$$ |  $$ |\$$$$$$$ |$$$$$$$  |$$ |  $$ |
\__|   \_______|   \_/    \__| \_______| \______/ \__|  \__|\__|  \__| \_______|\_______/ \__|  \__|
''', 'red')
    return banner

def get_random_user_agent():
    user_agent_list = []
    with open('user-agents.txt', 'r') as file:
        user_agent_list = file.readlines()
    user_agent = random.choice(user_agent_list).strip()
    return user_agent

def cmd_HashGenerator():
    URL = input(colored('\nEnter Favicon URL to generate Hash: ', 'yellow'))
    user_agent_choice = input(colored('\nChoose User Agent:\n1. Enter a custom User Agent\n2. Random User Agent\n> ', 'yellow'))

    if user_agent_choice == '1':
        user_agent = input(colored('\nEnter User Agent: ', 'yellow'))
    elif user_agent_choice == '2':
        user_agent = get_random_user_agent()
    else:
        print(colored('Invalid choice. Exiting.', 'red'))
        sys.exit(1)

    headers = {'User-Agent': user_agent}
    response = requests.get(URL, headers=headers)
    favicon = codecs.encode(response.content, "base64")
    print('\n')
    hash_value = mmh3.hash(favicon)
    print('----------')
    print(hash_value)
    print('----------')
    print('\n')
    shodan_link = colored(f'https://www.shodan.io/search?query=http.favicon.hash%3A{hash_value}', 'blue', attrs=['underline'])
    print(f'Tip: Use http.favicon.hash:{hash_value} on Shodan. Click the link below:')
    print(shodan_link)

    while True:
        try:
            choice = str(input(colored('\n[?] Do you want to continue? y/n\n> ', 'yellow'))).lower()
            if choice[0] == 'y':
                return cmd_HashGenerator()
            if choice[0] == 'n':
                sys.exit(0)
                break
            else:
                print(colored('Invalid Input', 'red'))
        except KeyboardInterrupt:
            print(colored('[!] Ctrl + C detected\n[!] Exiting', 'red'))
            sys.exit(0)
        except EOFError:
            print(colored('[!] Ctrl + D detected\n[!] Exiting', 'red'))
            sys.exit(0)

def main():
    print(logo())
    cmd_HashGenerator()

if __name__ == "__main__":
    main()
