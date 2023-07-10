
$$$$$$$$\                 $$\                               $$\   $$\                     $$\       
$$  _____|                \__|                              $$ |  $$ |                    $$ |      
$$ |   $$$$$$\ $$\    $$\ $$\  $$$$$$$\  $$$$$$\  $$$$$$$\  $$ |  $$ | $$$$$$\   $$$$$$$\ $$$$$$$\  
$$$$$\ \____$$\\$$\  $$  |$$ |$$  _____|$$  __$$\ $$  __$$\ $$$$$$$$ | \____$$\ $$  _____|$$  __$$\ 
$$  __|$$$$$$$ |\$$\$$  / $$ |$$ /      $$ /  $$ |$$ |  $$ |$$  __$$ | $$$$$$$ |\$$$$$$\  $$ |  $$ |
$$ |  $$  __$$ | \$$$  /  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$  __$$ | \____$$\ $$ |  $$ |
$$ |  \$$$$$$$ |  \$  /   $$ |\$$$$$$$\ \$$$$$$  |$$ |  $$ |$$ |  $$ |\$$$$$$$ |$$$$$$$  |$$ |  $$ |
\__|   \_______|   \_/    \__| \_______| \______/ \__|  \__|\__|  \__| \_______|\_______/ \__|  \__|

Author: Biraj Baishya
Twitter: @brutexploiter
Description: This tool calculates the FaviconHash value of a favicon to help hunt websites on Shodan.

FaviconHash is a Python script that leverages the mmh3 library to calculate the hash value of a favicon image. The script can be used to identify unique hash values associated with phishing websites. By searching for these hash values on Shodan using the "http.favicon.hash:<hash>" query, potential phishing websites can be discovered.

To use the FaviconHash tool, follow these steps:
1. Run the script and provide the URL of the favicon image.
2. Choose a user agent to be used in the HTTP request headers.
   - Option 1: Enter a custom user agent of your choice.
   - Option 2: Generate a random user agent from a list of predefined user agents.
3. The script will fetch the favicon image using the provided URL and the chosen user agent.
4. The favicon image will be encoded and the MurmurHash value will be calculated.
5. The calculated hash value will be displayed.
6. You can use the generated hash value with the "http.favicon.hash:<hash>" query on Shodan to hunt for potential phishing sites.
7. The script will prompt for continuation, allowing you to calculate hashes for multiple favicons.

Please note that the "user-agents.txt" file is required in the same directory as the script to generate random user agents. Make sure to update the "user-agents.txt" file with a list of valid user agents.

Disclaimer: This tool should be used responsibly and in compliance with all applicable laws and regulations. It is essential to respect the terms of service and the privacy policies of websites when using this tool for any purpose.

