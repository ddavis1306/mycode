#!/usr/bin/env python3

"""TESTING IF CONDITIONALS"""


#CREATE A STRING HOSTNAME

hostname = "MTG"

#test w/ if statement

if hostname == "MTG":
    print(f"hostname is indeed {hostname}")

#enter hostname
hostname = input("plz enter hostname --->:")
#force hostname to uppercase if true, print hostname if false print not a good hostname
if hostname.upper() == "MTG":
    print(f"hostname is {hostname}")
else:
    print(f"{hostname} is not a good hostname")

