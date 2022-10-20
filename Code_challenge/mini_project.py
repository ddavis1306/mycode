#!/usr/bin/env python3
"""MINI PROJECT | ddavis1306@gmail.com
check water tank levels with if else and while"""

def main():
  #checks to ensure the input is an integer. if not check error.
  while True:
    try:
      temperature = int(input("whats my fav temp? "))
      break
    except ValueError:
      print("please only enter numbers")
      
  while temperature != 65:
    #if the temp isnt 65 keep the script running
    if int(temperature) >= 66:
        temperature = input(f"{temperature}° is waaaaaay too hot \nWhats my fav temp? ")

    if int(temperature) == 65:
      print(f"its PERFECT WEATHER! I love when its {temperature}° and sunny")
      exit()

    elif int(temperature) <= 30:
      temperature = input(f"{temperature}° is waaaaaay too cold \nWhats my fav temp? ")

    if int(temperature) <= 64:
      temperature = input(f"{temperature}° is too cold \nWhats my fav temp? ")


if __name__ == "__main__":
    main()
