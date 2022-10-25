#!/usr/bin/env python3
"""NOT FINISHED LAB 63"""
#script to search and stop on first match
import os


## define a func that stops searching on 1st match
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

lookfor = input("what am i looking for? ")
lookwhere = input("what is the path in which i should searc")
print (find(lookfor, lookwhere))
