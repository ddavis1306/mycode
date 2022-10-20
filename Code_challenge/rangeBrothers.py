#!/usr/bin/env python3
import time

"""99 bottles song lab use range and a for loop"""
def main():
    while True:
        try:
            num_beers = int(input("enter in amount of beers:\n"))
            break
        except ValueError:
            print("please only enter numbers")
    a = "Bottles of beer on the wall!"
    b = "Bottles of beer! You take one down, pass it around!"
    if num_beers < 100:
        for i in range(num_beers, -1, -1):
            print(f"{i} {a}")
            print(f"{i} {b}")
            print(f"{i} {a}")
            time.sleep(.8)
    else:
        print("too many beers")
main()
