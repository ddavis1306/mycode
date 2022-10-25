#!/usr/bin/env python3

"""explore reading files | create obj in read mode"""

configfile = open("vlanconfig.cfg", "r")

#disp file to screen
print(configfile.read())

##close file
configfile.close()

##re-create file obj to explore new method
configfile = open("vlanconfig.cfg", "r")

#make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)


#iterate thru configlist
for x in configlist:
    print(x)

configfile.close()
