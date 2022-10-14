#!/usr/bin/env Python3

import ssl


def main():
    vendor_input = input("iphone or android: ")
    print(vendor_input)
    if(vendor_input == "iphone" or "android"):
        print("good choice! I love, " + vendor_input);
    else:
            print("please enter valid answer")
main()