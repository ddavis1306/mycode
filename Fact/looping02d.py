#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with' | now we are sorting .com and 
   .org domains in separate folders"""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # loop over lines
    for lines in dnsfile:
        lines = lines.strip('\n')

        if lines.endswith("org"):
            with open("org-domain.txt", "a") as linefile:
                linefile.write(lines + "\n")

        elif lines.endswith("com"):
            with open("com-domain.txt", "a") as linefile:
                linefile.write(lines + "\n")
    # no need to close our file - closed automatically
