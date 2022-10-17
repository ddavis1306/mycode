#!/usr/bin/env python3

def main():

	list1=["cisco_abc","arista_acd","cisco_iso"]
	list2=["juniper"]
	list3=["192.168.1.1", "10.1.1.1"]
	list1.extend(list2)
	list1.append(list3)
	print(list1)
	print(list1[1])
	print(list1[4][0])
main()
