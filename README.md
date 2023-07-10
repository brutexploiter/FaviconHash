# FaviconHash

FaviconHash is a Python script that leverages the mmh3 library to calculate the hash value of a favicon image. The script can be used to identify unique hash values associated with websites. By searching for these hash values on Shodan using the "http.favicon.hash:<hash>" query, websites can be discovered.

<a href="https://twitter.com/brutexploiter"><img src="https://img.shields.io/twitter/follow/brutexploiter.svg?logo=twitter"></a>
</p>

### What is MurMurHash?
MurmurHash is a non-cryptographic hash function suitable for general hash-based lookup. The name comes from two basic operations, multiply (MU) and rotate (R), used in its inner loop. The current version is MurmurHash3 which yields a 32-bit or 128-bit hash value. When using 128-bits, the x86 and x64 versions do not produce the same values, as the algorithms are optimized for their respective platforms. MurmurHash3 was released alongside SMHasher—a hash function test suite.

Further reading on: https://en.wikipedia.org/wiki/MurmurHash

# Install FaviconHash
```
git clone https://github.com/brutexploiter/FaviconHash.git
cd FaviconHash
pip install -r requirements.txt
python FaviconHash.py
```
# Usage
To use the FaviconHash tool, follow these steps:
1. Run the script and provide the URL of the favicon image.
2. Choose a user agent to be used in the HTTP request headers.
   - Option 1: Enter a custom user agent of your choice.
   - Option 2: Generate a random user agent from a list of predefined user agents.
3. The script will fetch the favicon image using the provided URL and the chosen user agent.
4. The favicon image will be encoded and the MurmurHash value will be calculated.
5. The calculated hash value will be displayed.
6. You can use the generated hash value with the "http.favicon.hash:<hash>" query on Shodan to hunt for potential websites.
7. The script will prompt for continuation, allowing you to calculate hashes for multiple favicons.

Please note that the "user-agents.txt" file is required in the same directory as the script to generate random user agents. Make sure to update the "user-agents.txt" file with a list of valid user agents.

Disclaimer: This tool should be used responsibly and in compliance with all applicable laws and regulations. It is essential to respect the terms of service and the privacy policies of websites when using this tool for any purpose.

