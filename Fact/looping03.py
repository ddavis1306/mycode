#!/usr/bin/env python3

"""looping across range w/ UUID"""

#Allows us to generate UUID
import uuid

howmany = int(input("how many UUID should be generated "))

print("generating UUIDS")

for rando in range(howmany):
    print(uuid.uuid4())