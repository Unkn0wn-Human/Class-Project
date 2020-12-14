#Gets weather from Openweathermap.org for the zipcode the user provided


#intro

import requests
import json
from urllib.request import urlopen


def menu_screen():
    print("Weather Finder Menu")
    print("[1] weather for a zipcode")
    print("[2] QUIT")


def cityName():
   city = input("What zipcode: ")
   with urlopen('https://api.openweathermap.org/data/2.5/weather?q={}&appid=0c626c7fd13afd854621cb0ed3a0c9ec'.format(city)) as response:
       source = response.read() 
   data = json.loads(source)
   print(json.dumps(data, indent=2))
   #print(data['list']['weather'])

print("Welcome to Weather Finder!")
run = 'yes'
while run == 'yes':
    menu_screen()
    chose = int(input("Please choose an option: "))
    if chose == 1:
       cityName()
    if chose == 2:
       print("Thanks for trying out weather finder")
       run = 'no'


    

