#!/usr/bin/env python3

""" Review of TRY and EXCEPT logic | darryl d"""

# start with an infinite loop
while True:
    try:
        print("enter file name:\n")
        name = input()
        with open(name, "w") as myfile:
            myfile.write("No problems with that file name.")
        break
    except:
        print("Error with that file name! Try again")
