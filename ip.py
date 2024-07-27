import urllib.request
import json
import os
import random  # Importing the random module
import threading
import requests

getIP = input("[?] Введите IP -> ")
url = "https://ipinfo.io/" + getIP + "/json"

try:
    getInfo = urllib.request.urlopen(url)
    infoList = json.load(getInfo)  # Assign a value to infoList here

    print("-" * 60)
    print("IP: ", infoList["ip"])  # Use infoList after assigning a value

    print("City: ", infoList["city"])  # Access other elements of infoList
    print("Region: ", infoList["region"])
    print("Country: ", infoList["country"])

except:
    print("\n[!] Ошибка IP не найден! - [!]\n")

def whoisIPinfo(ip):
    try:
        myCommand = "whois " + getIP
        whoisInfo = os.popen(myCommand).read()
        return whoisInfo
    except:
        return "\n [!] -- Ошибка -- [!] \n"
back = input("[!] Нажмите ENTER для возврата в главное меню\n")
os.system("clear")
os.system("python main.py")