import json
import sys
import requests
import datetime
from time import sleep
from colorama import Style, Fore
from requests import post

print(Fore.BLUE+"Created by czQery")

with open("config.json", "r+", encoding="utf-8") as config_file:
    config = json.load(config_file)
    config_file.close()
try:
    message = config["message"]
    target = config["target"]
    session_id = config["session_id"]
    login_secure = config["login_secure"]
    machine_auth = config["machine_auth"]
except:
    ct = datetime.datetime.now()
    print(Fore.BLUE+f"[{ct.hour}:{ct.minute}:{ct.second}]"+Fore.RED+" Config error!")
    sys.exit()
ct = datetime.datetime.now()
print(Fore.BLUE+f"[{ct.hour}:{ct.minute}:{ct.second}]"+Fore.GREEN+" Config loaded!")


while True:
    profile = requests.get(f"https://steamcommunity.com/profiles/{target}/")

    if not message in profile.text:
        data = {"comment": message, "sessionid": session_id, "feature2": -1}
        cookies = {"sessionid": session_id, "steamLoginSecure": login_secure, "steamMachineAuth": machine_auth}
        resp = post(f"https://steamcommunity.com/comment/Profile/post/{target}/-1", data=data, cookies=cookies)

        if (resp.json().get("success") is True):
            ct = datetime.datetime.now()
            print(Fore.BLUE+f"[{ct.hour}:{ct.minute}:{ct.second}]"+Fore.GREEN+ " Success!")
        else:
            ct = datetime.datetime.now()
            print(Fore.BLUE+f"[{ct.hour}:{ct.minute}:{ct.second}]"+Fore.RED+ " Failed!")
    sleep(300)
