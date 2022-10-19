#!/usr/bin/env python3

"""ip check || also checks if gateway ip was entered"""

ipchk = input("Enter an IP addr:")

if ipchk !="192.168.1.1":
    print(f"{ipchk} was a good IP addr")
elif ipchk == "192.168.1.1":
    print(f"ummm excuse me {ipchk} is the gateway")
else:
    print("invalid input, try again")
