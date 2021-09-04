import requests
from colorama import Fore
import pyfiglet
import time

result = pyfiglet.figlet_format("Replit Username Checker")
print(result)
time.sleep(1)
print("made by quik#0001")
time.sleep(1)
url = "https://www.replit.com/@"
username = input("What\'s the username you want to check?\n")
response = requests.get(url + username)
status = response.status_code
if status == 200:
  print(Fore.RED + "Unavailable!" + " " + "@" +  username)
  time.sleep(1)
  print(Fore.WHITE + "The url to this user is:" + " " + url + username)
elif status == 404:
  print(Fore.GREEN + "Available!" + " " + "@" + username) 
