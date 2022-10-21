#!/usr/bin/env python3

"""using for() range and with"""

#open file in read mode
dnsfile = open("dnsservers.txt", "r")

#create list of lines
dnslist = dnsfile.readlines()

#loop over lines
for svr in dnslist:
#svr is a variable set for each item in dnsfile
#print and end w/o a new line
    print(svr, end="")#the txt file already has line breaks

#close file
dnsfile.close()
