#!/usr/bin/env python3
"""farm challenge"""
from farmList import farms
ne_farm = farms[0]["agriculture"]
w_farm = farms[1]["agriculture"]
se_farm = farms[2]["agriculture"]

chooseFarm = input("choose a farm\n(NE Farm, W Farm, SE Farm):\n")
if chooseFarm == "NE Farm":
    for i in ne_farm:
        print(i)
elif chooseFarm == "W Farm":
    for i in w_farm:
        print(i)
elif chooseFarm == "SE Farm":
    for i in se_farm:
        print (i)
else:
    print("please enter a valid entry")

