import argparse
import mmh3
import requests
import codecs
import random
import sys
from termcolor import colored
import shodan

def get_random_user_agent():
    """Returns a random user agent from user-agents.txt."""
    with open('user-agents.txt', 'r') as file:
        user_agent_list = file.readlines()
    return random.choice(user_agent_list).strip()

def fetch_favicon_hash(url, user_agent=None):
    """Fetches the favicon, calculates its hash, and returns the hash."""
    headers = {}
    if user_agent:
        headers['User-Agent'] = user_agent
    response = requests.get(url, headers=headers)
    favicon = codecs.encode(response.content, "base64")
    return mmh3.hash(favicon)

def search_shodan(hash_value, shodan_api_key):
    """Searches Shodan for the given hash value and prints the results."""
    api = shodan.Shodan(shodan_api_key)
    query = f"http.favicon.hash:{hash_value}"
    try:
        results = api.search(query)
        print(colored(f'\nShodan search results for hash {hash_value}:\n', 'green'))
        for result in results['matches']:
            print(colored(f"IP: {result['ip_str']}, Port: {result['port']}, Hostnames: {result['hostnames']}", 'green'))
    except shodan.APIError as e:
        print(colored(f'Error: {e}', 'red'))

def main():
    parser = argparse.ArgumentParser(prog='favicon.py', description='FaviconHash - Calculate and search favicon hash on Shodan.', add_help=False)
    parser.add_argument('-u', '--url', metavar='<URL>', type=str, help='URL of the favicon')
    parser.add_argument('-a', '--api-key', metavar='<SHODAN_API_KEY>', type=str, help='Specify Shodan API key')
    parser.add_argument('-r', '--random-agent', action='store_true', help='Use a random user agent')
    parser.add_argument('-c', '--custom-agent', metavar='<CUSTOM_AGENT>', type=str, help='Specify a custom user agent')
    parser.add_argument('-h', '--help', action='store_true', help='Show this help message and exit')
    args = parser.parse_args()

    if args.help:
        print('''Usage: favicon.py -u <URL> -a <SHODAN_API_KEY>

FaviconHash - Calculate and search favicon hash on Shodan.

Commands:
  -u, --url    URL of the favicon
  -a, --api-key  Specify Shodan API key

Options:
  -h, --help            Show this help message and exit
  -r, --random-agent    Use a random user agent
  -c, --custom-agent    Specify a custom user agent''')
        sys.exit(0)

    if not any(vars(args).values()):
        print("No command supplied. Use -h/--help to know more.")
        sys.exit(1)

    if not args.url or not args.api_key:
        parser.print_help()
        sys.exit(1)

    if args.random_agent:
        user_agent = get_random_user_agent()
    elif args.custom_agent:
        user_agent = args.custom_agent
    else:
        user_agent = None

    hash_value = fetch_favicon_hash(args.url, user_agent)
    print('\n----------')
    print(hash_value)
    print('----------\n')

    shodan_link = colored(f'https://www.shodan.io/search?query=http.favicon.hash%3A{hash_value}', 'blue', attrs=['underline'])
    print(f'Tip: Use http.favicon.hash:{hash_value} on Shodan. Click the link below:')
    print(shodan_link)

    search_shodan(hash_value, args.api_key)

if __name__ == "__main__":
    main()
