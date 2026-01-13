#!/usr/bin/env python3

from requests_tor import RequestsTor

logo = r"""
 ____             _        _   _ ____  _
|  _ \  __ _ _ __| | _____| | | |  _ \| |
| | | |/ _` | '__| |/ / __| | | | |_) | |
| |_| | (_| | |  |   < (__| |_| |  _ <| |___
|____/ \__,_|_|  |_|\_\___|\___/|_| \_\_____|
"""
print(logo)


requests = RequestsTor(tor_ports=(9050,), tor_cport=9051)

onion_url = input("\nInsert .onion URL to scrape: ")

onion_site = requests.get(onion_url)

print("Here's your onion!: 🧅\n\n", onion_site.text)

