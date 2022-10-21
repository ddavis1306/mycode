#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'"""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # create list of lines
    dnslist = dnsfile.readlines()
    # loop over lines
    for lines in dnslist:
        #print and end without a newline
        print(lines, end="")

# no need to close our file - closed automatically
