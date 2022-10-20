#!/usr/bin/env python3
def main():


    name= input("What is your name?\n>")
    mylist= [1,2,3,4,5, "Python"]

# This is what you should see when print runs-
# Hi <name>! Welcome to Day 2 of Python Training!
    print(f"Hi {name.capitalize()} ! Welcome to Day {mylist[1]} of {mylist[5]}  Training!")

main()