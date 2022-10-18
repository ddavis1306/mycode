#!/usr/bin/env python3
""" complex lists """

def main():

    list1=["cisco_abc","arista_acd","cisco_iso"]
    list2=["juniper"]
    list3=["192.168.1.1", "10.1.1.1"]
    list1.extend(list2)
    list1.append(list3)
    print(f"This is list 1 with list2 extended onto it and list3 appened onto it: \n{list1}")
    print(f"This is list one, all the same rules but with the second index is list1: \n{list1[1]}")
    print(f"This is list 1 targeting the forth index and the first index within that list:\n{list1[4][0]}")

main()
