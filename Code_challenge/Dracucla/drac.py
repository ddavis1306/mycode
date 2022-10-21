#!/usr/bin/env python3
vampCount = 0
searched_word = input("please enter what word you want to find:\n")
with open("dracula.txt", "r") as dractxt:
    with open("vampThings.txt", "w") as vfile:
        for line in dractxt:
            if searched_word  in line.lower():
                vampCount += 1
                vfile.write(line)
    print(f"The word Vampire appeared {vampCount} times!")
