import time
import json
import random

time1 = time.time()
while True:
    time2 = time.time()
    if time2-time1 >= 3600:
        with open('bd_telebot.json', 'r') as file:
            data = json.load(file)
        for i in data:
            p = data[i]["power"]
            b = data[i]["tgcoins"] + p
            data[i]["tgcoins"] = b
            with open('bd_telebot.json', 'w') as file:
                json.dump(data, file, indent=4)
        with open('bd_telebot.json', 'r') as file:
            data = json.load(file)
        for i in data:
            if "reffer" in data[i]["dop2"]:
                for r in data[i]["dop2"]["reffer"]:
                    po = data[r]["power"] * 0.2
                    ba = data[i]["tgcoins"] + po
                    data[i]["tgcoins"] = ba
                    with open('bd_telebot.json', 'w') as file:
                        json.dump(data, file, indent=4)
            

        time1 = time.time()