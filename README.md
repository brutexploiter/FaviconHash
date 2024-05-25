# FaviconHash
[![Python 3](https://img.shields.io/badge/python-3-yellow.svg)](https://www.python.org/)
[![License](https://img.shields.io/github/license/brutexploiter/FaviconHash)](https://github.com/brutexploiter/FaviconHash/blob/main/LICENSE)


![image](https://github.com/brutexploiter/FaviconHash/assets/88744417/ffc72f01-6eb0-4d51-a749-4a6f6a0fcb7c)




FaviconHash is a Python script that leverages the mmh3 library to calculate the hash value of a favicon image. The script can be used to identify unique hash values associated with websites. By searching for these hash values on Shodan using the "http.favicon.hash:<hash>" query, websites can be discovered.

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

```
favicon.py -u <URL> -a <SHODAN_API_KEY>
```
FaviconHash - Calculate and search favicon hash on Shodan.
```
Commands:
-u, --url: URL of the favicon
-a, --api-key: Specify Shodan API key

Options:
-h, --help: Show this help message and exit
-r, --random-agent: Use a random user agent
-c, --custom-agent: Specify a custom user agent
```

Example:

```
python favicon.py -u https://example.com/favicon.ico -a YOUR_SHODAN_API_KEY -r
```
Please note that the "user-agents.txt" file is required in the same directory as the script to generate random user agents. Make sure to update the "user-agents.txt" file with a list of valid user agents.

Disclaimer: This tool should be used responsibly and in compliance with all applicable laws and regulations. It is essential to respect the terms of service and the privacy policies of websites when using this tool for any purpose.

## Planned Features
- Shodan Integration (Coming Soon)

## Credits
- [Viral Maniar](https://github.com/Viralmaniar/MurMurHash)
[![Twitter](https://img.shields.io/twitter/follow/maniarviral.svg?logo=twitter)](https://twitter.com/maniarviral)
