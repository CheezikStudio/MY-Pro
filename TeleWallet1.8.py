# -*- coding: utf8 -*-

import telebot 
import time
import json
import random
import heapq
from telebot import types
from pyKeksik import KeksikApi
from types import *
import yfinance as yahooFinance
def main():
    
    
    while True:
        w = 1
        try:
            
            

            bot = telebot.TeleBot('5322808959:AAGiPpfLWHbnALO4Dz6TdIxdC1CmKQlvzPI')
            @bot.message_handler(commands=["start"])

            def start(message, res=False):
                
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if idtg not in data:
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    name = str(message.chat.first_name)
                    idtg = str(message.from_user.id)
                    
                    absd = "qwertyuiopasdfghjklxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
                    q = ""
                    for i in range(1, 14):
                        a = random.randint(1, 60)
                        q = q + absd[a]
                    
                    rbr = {"idcoin": i, "name": name, "tgcoins" : 100, "email": "❌", "token": q, "nikname": None, "power": 0, "dop1": [], "dop2": {}, "dop3": ""}
                    data[idtg] = rbr
                    with open('bd_telebot.json', 'w') as file:
                        json.dump(data, file, indent=4)
                if " " in message.text:
                    
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    t = 0
                    for i in data:
                        try:
                            if idtg in data[i]["dop2"]["reffer"]:
                                t = 1
                        except:
                            e = 1
                    if t != 1:
                        for i in data:

                            if i == str(message.text.split()[1]):
                                pol1 = data[i]["tgcoins"] + 300
                                pol2 = data[idtg]["tgcoins"] + 300
                                pol22 = data[i]["power"] + 0.5
                                
                                reff = data[i]["dop2"]["reffer"].append(idtg)
                                data[i]["tgcoins"] = pol1
                                data[idtg]["tgcoins"] = pol2
                                data[idtg]["power"] = pol22
                                
                                with open('bd_telebot.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                                bot.send_message(message.chat.id, f'For the transition you received: 300 Telecoins!')
                                bot.send_message(i, f'Through your referral link, I have registered: {data[idtg]["name"]}\nThe bonus is already on the balance!')
                                break
                            
                    
                if "sub" not in data[idtg]["dop2"]:
                        
                        data[idtg]["dop2"]["sub"] = "❌"
                        with open('bd_telebot.json', 'w') as file:
                            json.dump(data, file, indent=4)
                if "med" not in data[idtg]["dop2"]:
                        
                    data[idtg]["dop2"]["med"] = []
                    with open('bd_telebot.json', 'w') as file:
                        json.dump(data, file, indent=4)




                

                if data[idtg]["dop3"] == 'ru':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Отправить🛫')
                    btn2 = types.KeyboardButton('Майнинг📊')
                    btn3 = types.KeyboardButton('Получить🛬')
                    btn4 = types.KeyboardButton('Лучшие по балансу🏆')
                    btn5 = types.KeyboardButton('Профиль🙍‍♂')
                    btn6 = types.KeyboardButton('Лучшие по мощности🏆')
                    btn7 = types.KeyboardButton('Сервисы📚')
                    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
                    bot.send_message(message.chat.id, f'''
            Информация
        Имя: {data[idtg]["name"]}🙍‍♂
        Почта:  {data[idtg]["email"]}
        Баланс:  {data[idtg]["tgcoins"]}💰
        Мощность: {data[idtg]["power"]}𝘁𝗰/𝗵⚡
        Нажми на кнопку👇🏻
                    ''',  reply_markup=markup)
                    #перевод человека
                    bot.register_next_step_handler(message, wallet_ru)
                else:   
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Send🛫')
                    btn2 = types.KeyboardButton('Bank🏛')
                    btn3 = types.KeyboardButton('Get🛬')
                    btn4 = types.KeyboardButton('Top by balance🏆')
                    btn5 = types.KeyboardButton('Profile🙍‍♂')
                    btn6 = types.KeyboardButton('Top by referrals🏆')
                    btn7 = types.KeyboardButton('Events👾')
                    btn8 = types.KeyboardButton('Services📚')
                    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
                    bot.send_message(message.chat.id, f'''
                        𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

                𝗡𝗮𝗺𝗲: {data[idtg]["name"]}🙍‍♂
                𝗘𝗺𝗮𝗶𝗹:  {data[idtg]["email"]}
                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                
                𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    #перевод человека
                    bot.register_next_step_handler(message, wallet)

            
            def wallet(message):
                
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Send🛫':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'Write the token of the wallet to which you want to make the transfer:',  reply_markup=markup)
                    bot.register_next_step_handler(message, otpr)
                elif message.text == 'Get🛬':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'𝗬𝗼𝘂𝗿 𝘄𝗮𝗹𝗹𝗲𝘁 𝘁𝗼𝗸𝗲𝗻:  <code>{data[idtg]["token"]}</code>\n𝗬𝗼𝘂 𝗰𝗮𝗻 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝘁𝗼𝗸𝗲𝗻 𝘁𝗼 𝗴𝗲𝘁 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻𝘀 𝗳𝗿𝗼𝗺 𝗼𝘁𝗵𝗲𝗿 𝗽𝗲𝗼𝗽𝗹𝗲🔥\n𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝘁𝗼𝗸𝗲𝗻 𝘁𝗼 𝗰𝗼𝗽𝘆', parse_mode='HTML',  reply_markup=markup)
                    bot.register_next_step_handler(message, start)
                elif message.text == 'Top by referrals🏆':
                    top1 = []
                    top2 = {}
                    for i in data:
                        try:
                            b = len(data[i]["dop2"]["reffer"])
                            n = data[i]["name"]
                            a = (b, n)
                            top1.append(a)
                        except:
                            r = 1
                    top2 = heapq.nlargest(3, top1)
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    
                    bot.send_message(message.chat.id, f'''
                    𝗧𝗼𝗽 𝗯𝘆 𝗿𝗲𝗳𝗲𝗿𝗿𝗮𝗹𝘀🏆
            🥇 {top2[0][1]} | {top2[0][0]} 𝗽𝗲𝗼𝗽𝗹𝗲
            🥈 {top2[1][1]} | {top2[1][0]} 𝗽𝗲𝗼𝗽𝗹𝗲
            🥉 {top2[2][1]} | {top2[2][0]} 𝗽𝗲𝗼𝗽𝗹𝗲

            𝗧𝗵𝗲 𝘁𝗼𝗽 𝟯 𝗽𝗲𝗼𝗽𝗹𝗲 𝘄𝗶𝗹𝗹 𝗿𝗲𝗰𝗲𝗶𝘃𝗲 % 𝗶𝗻 𝘁𝗵𝗲 𝗯𝗮𝗻𝗸 𝗲𝘃𝗲𝗿𝘆 𝘄𝗲𝗲𝗸. 𝗧𝗵𝗲 𝗿𝗮𝘁𝗶𝗻𝗴 𝗶𝘀 𝗻𝗼𝘁 𝗿𝗲𝘀𝗲𝘁!
            🥇 +𝟮%
            🥈 +𝟭%
            🥉 +𝟬.𝟱%
            𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, start)
                elif message.text == 'Top by balance🏆':
                    top1 = []
                    top2 = {}
                    for i in data:
                        try:
                            b = data[i]["tgcoins"] + data[i]["dop2"]["bank"]
                            n = data[i]["name"]
                            a = (b, n)
                            top1.append(a)
                        except:
                            b = data[i]["tgcoins"]
                            n = data[i]["name"]
                            a = (b, n)
                            top1.append(a)
                    top2 = heapq.nlargest(5, top1)
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    𝗧𝗼𝗽 𝗯𝘆 𝗯𝗮𝗹𝗮𝗻𝗰𝗲🏆
            🥇 {top2[0][1]} | {top2[0][0]} telecoins
            🥈 {top2[1][1]} | {top2[1][0]} telecoins
            🥉 {top2[2][1]} | {top2[2][0]} telecoins
            🏅 {top2[3][1]} | {top2[3][0]} telecoins
            🏅 {top2[4][1]} | {top2[4][0]} telecoins
            𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, start)

                elif message.text == 'Profile🙍‍♂':
                    if "sub" not in data[idtg]["dop2"]:
                        
                        data[idtg]["dop2"]["sub"] = "❌"
                        with open('bd_telebot.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    if "med" not in data[idtg]["dop2"]:
                        
                        data[idtg]["dop2"]["med"] = []
                        with open('bd_telebot.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Change Email')
                    btn2 = types.KeyboardButton('Change Nickname')
                    btn3 = types.KeyboardButton('Referral program')
                    btn4 = types.KeyboardButton('Subscription')
                    btn5 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    n = '\n'
                    bot.send_message(message.chat.id, f'''
                𝗣𝗿𝗼𝗳𝗶𝗹𝗲🙍‍♂
𝗡𝗮𝗺𝗲: {data[idtg]["name"]}🙍‍♂
𝗘𝗺𝗮𝗶𝗹:  {data[idtg]["email"]}
𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻: {data[idtg]["dop2"]["sub"]}
𝗠𝗲𝗱𝗮𝗹𝘀: 
{n.join(data[idtg]["dop2"]["med"])}

𝗪𝗵𝗮𝘁 𝗱𝗼 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼?
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, prof)
                
                elif message.text == 'Bank🏛':
                    if "bank" not in data[idtg]["dop2"]:
                        
                        bot.send_message(message.chat.id, f'''
Here you can receive interest every day from the deposit amount!
Example:

On the bank - 100,000 Telecoins
This means that with 1 percent you will receive 1,000 Telecoins every day. These coins will end up in the bank.

How do I get these % per day?

- Press the 'Receive%' button every day!

How to increase the interest?

- Invite people by referral link

Перевод:

Здесь вы можете получать проценты каждый день от суммы вклада!
Пример:

В банке - 100.000 Telecoins 
Это значит что с  1 процентом вы будете получать каждый день по 1.000 Telecoins. Эти монеты попадут в банк.

Как получать эти % в день?

- Нажимать каждый день на кнопку 'Receive %'! 

Как увеличить проценты?

- Приглашать людей по реферальной ссылке
                        ''')
                        data[idtg]["dop2"]["bank"] = 0
                        data[idtg]["power"] = 1
                        with open('bd_telebot.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    if "bank_time" not in data[idtg]["dop2"]:
                        q = time.time()
                        data[idtg]["dop2"]["bank_time"] = q
                        with open('bd_telebot.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    if "bank_ac" not in data[idtg]["dop2"]:
                        
                        data[idtg]["dop2"]["bank_ac"] = {}
                        with open('bd_telebot.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Replenish📥')
                    btn2 = types.KeyboardButton('Receive %')
                    btn22 = types.KeyboardButton('Bring out📤')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn22, btn7)
                    bot.send_message(message.chat.id, f'''
                    𝗕𝗮𝗻𝗸🏛

                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                𝗜𝗻 𝘁𝗵𝗲 𝗕𝗮𝗻𝗸: {data[idtg]["dop2"]["bank"]}🏛
                𝗣𝗲𝗿𝗰𝗲𝗻𝘁𝗮𝗴𝗲𝘀: {data[idtg]["power"]}%

                𝗖𝗵𝗼𝗼𝘀𝗲 𝘄𝗵𝗮𝘁 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼👇🏻

                
                        ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, bank)



                elif message.text == 'Events👾':
                    if "events_coin" not in data[idtg]["dop2"]:
                        data[idtg]["dop2"]["events_coin"] = 0
                        with open('bd_telebot.json', 'w') as file:
                            json.dump(data, file, indent=4)
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Shop🛒')
                    btn2 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
                    𝗘𝘃𝗲𝗻𝘁𝘀👾

                𝗛𝗮𝗹𝗹𝗼𝘄𝗲𝗲𝗻 𝗘𝘃𝗲𝗻𝘁 𝟮𝟬𝟮𝟮🎃

                𝗘𝘃𝗲𝗻𝘁 𝗰𝗼𝗶𝗻𝘀:  {data[idtg]["dop2"]["events_coin"]}

                𝗔𝗹𝗹 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗮𝗯𝗼𝘂𝘁 𝘁𝗵𝗲 𝗲𝘃𝗲𝗻𝘁𝘀 𝗶𝘀 𝗵𝗲𝗿𝗲: https://vk.com/tele_ivents
                
                𝗖𝗵𝗼𝗼𝘀𝗲 𝘄𝗵𝗮𝘁 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼👇🏻
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, events)



                elif message.text == 'Services📚':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('TeleShop')
                    btn2 = types.KeyboardButton('TeleGame')
                    btn22 = types.KeyboardButton('TeleStats')
                    btn3 = types.KeyboardButton('The development team/website')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn22, btn3, btn7)
                    bot.send_message(message.chat.id, f'''
                    𝗧𝗵𝗲𝘀𝗲 𝗮𝗿𝗲 𝗮𝗹𝗹 𝗼𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻 𝘀𝗲𝗿𝘃𝗶𝗰𝗲𝘀! 
                    𝗦𝗲𝗹𝗲𝗰𝘁 𝗼𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝗺 𝗼𝗿 𝗿𝗲𝘁𝘂𝗿𝗻 𝘁𝗼 𝘁𝗵𝗲 𝗺𝗲𝗻𝘂)
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, serv)
                elif message.text == 'Admin' and idtg == "1058097307" or idtg == "1052237329":
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('База данных')
                    btn2 = types.KeyboardButton('Рассылка')
                    btn3 = types.KeyboardButton('Ивенты')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3, btn7)
                    bot.send_message(message.chat.id, f'''
                    Админ меню:
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, admin)
                else:
                    bot.send_message(message.chat.id, f"I didn't understand what you wrote) Write: /start")
            def events(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Send🛫')
                    btn2 = types.KeyboardButton('Bank🏛')
                    btn3 = types.KeyboardButton('Get🛬')
                    btn4 = types.KeyboardButton('Top by balance🏆')
                    btn5 = types.KeyboardButton('Profile🙍‍♂')
                    btn6 = types.KeyboardButton('Top by referrals🏆')
                    btn7 = types.KeyboardButton('Events👾')
                    btn8 = types.KeyboardButton('Services📚')
                    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
                    bot.send_message(message.chat.id, f'''
                        𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

                𝗡𝗮𝗺𝗲: {data[idtg]["name"]}🙍‍♂
                𝗘𝗺𝗮𝗶𝗹:  {data[idtg]["email"]}
                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                
                𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    #перевод человека
                    bot.register_next_step_handler(message, wallet)
                elif message.text == 'Shop🛒':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('+ 0.5% in bank - 50 Event coins')
                    btn2 = types.KeyboardButton('Custom token - 150 Event coins')
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                    𝗛𝗮𝗹𝗹𝗼𝘄𝗲𝗲𝗻 𝗘𝘃𝗲𝗻𝘁 𝟮𝟬𝟮𝟮🎃

                𝗘𝘃𝗲𝗻𝘁 𝗰𝗼𝗶𝗻𝘀:  {data[idtg]["dop2"]["events_coin"]}💰
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, events_shop)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    bot.send_message(message.chat.id, f'An error has occurred! Try again!',  reply_markup=markup)
                    bot.register_next_step_handler(message, backev)
            def events_shop(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Shop🛒')
                    btn2 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
                    𝗘𝘃𝗲𝗻𝘁𝘀👾

                𝗛𝗮𝗹𝗹𝗼𝘄𝗲𝗲𝗻 𝗘𝘃𝗲𝗻𝘁 𝟮𝟬𝟮𝟮🎃

                𝗘𝘃𝗲𝗻𝘁 𝗰𝗼𝗶𝗻𝘀:  {data[idtg]["dop2"]["events_coin"]}

                𝗔𝗹𝗹 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗮𝗯𝗼𝘂𝘁 𝘁𝗵𝗲 𝗲𝘃𝗲𝗻𝘁𝘀 𝗶𝘀 𝗵𝗲𝗿𝗲: https://vk.com/tele_ivents
                
                𝗖𝗵𝗼𝗼𝘀𝗲 𝘄𝗵𝗮𝘁 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼👇🏻
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, events)
                elif message.text == '+ 0.5% in bank - 50 Event coins':
                    if data[idtg]["dop2"]["events_coin"] >= 50:
                        pol1 = data[idtg]["dop2"]["events_coin"] - 50
                        pol2 = data[idtg]["power"] + 0.5
                        data[idtg]["dop2"]["events_coin"] = pol1
                        pol2 = data[idtg]["power"] = pol2
                        with open('bd_telebot.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'Purchase completed successfully✅',  reply_markup=markup)
                        bot.register_next_step_handler(message, backevs)
                    else:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f"You don't have enough coin events!",  reply_markup=markup)
                        bot.register_next_step_handler(message, backevs)
                elif message.text == 'Custom token - 150 Event coins':
                    if data[idtg]["dop2"]["events_coin"] >= 150:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'Token:',  reply_markup=markup)
                        bot.register_next_step_handler(message, token_e)
                    else:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f"You don't have enough coin events!",  reply_markup=markup)
                        bot.register_next_step_handler(message, backevs)
            def token_e(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('+ 0.5% in bank - 50 Event coins')
                    btn2 = types.KeyboardButton('Custom token - 150 Event coins')
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                    𝗛𝗮𝗹𝗹𝗼𝘄𝗲𝗲𝗻 𝗘𝘃𝗲𝗻𝘁 𝟮𝟬𝟮𝟮🎃

                𝗘𝘃𝗲𝗻𝘁 𝗰𝗼𝗶𝗻𝘀:  {data[idtg]["dop2"]["events_coin"]}💰
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, events_shop)
                else:
                    k = "d"
                    for i in data:
                        if data[i]["token"] == message.text:
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                            btn1 = types.KeyboardButton('Back👈🏻')
                            markup.add(btn1)
                            bot.send_message(message.chat.id, f"Such a token is already in use! Try Another One!",  reply_markup=markup)
                            bot.register_next_step_handler(message, backevs)
                            k = "s"
                            break
                    if k == "d":
                        pol1 = data[idtg]["dop2"]["events_coin"] - 150
                        pol2  =data[idtg]["token"] = message.text
                        data[idtg]["dop2"]["events_coin"] = pol1
                        pol2 = data[idtg]["token"] = pol2
                        with open('bd_telebot.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'Purchase completed successfully✅',  reply_markup=markup)
                        bot.register_next_step_handler(message, backevs)
            def backev(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                reply_markup = types.ReplyKeyboardRemove()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                btn1 = types.KeyboardButton('Shop🛒')
                btn2 = types.KeyboardButton('Back👈🏻')
                markup.add(btn1, btn2)
                bot.send_message(message.chat.id, f'''
                𝗘𝘃𝗲𝗻𝘁𝘀👾

            𝗛𝗮𝗹𝗹𝗼𝘄𝗲𝗲𝗻 𝗘𝘃𝗲𝗻𝘁 𝟮𝟬𝟮𝟮🎃

            𝗘𝘃𝗲𝗻𝘁 𝗰𝗼𝗶𝗻𝘀:  {data[idtg]["dop2"]["events_coin"]}

            𝗔𝗹𝗹 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗮𝗯𝗼𝘂𝘁 𝘁𝗵𝗲 𝗲𝘃𝗲𝗻𝘁𝘀 𝗶𝘀 𝗵𝗲𝗿𝗲:https://vk.com/tele_ivents
            
            𝗖𝗵𝗼𝗼𝘀𝗲 𝘄𝗵𝗮𝘁 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼👇🏻
                ''',  reply_markup=markup)
                bot.register_next_step_handler(message, events)
            def backevs(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                reply_markup = types.ReplyKeyboardRemove()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                btn1 = types.KeyboardButton('+ 0.5% in bank - 50 Event coins')
                btn2 = types.KeyboardButton('Custom token - 150 Event coins')
                btn3 = types.KeyboardButton('Back👈🏻')
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, f'''
                𝗛𝗮𝗹𝗹𝗼𝘄𝗲𝗲𝗻 𝗘𝘃𝗲𝗻𝘁 𝟮𝟬𝟮𝟮🎃

            𝗘𝘃𝗲𝗻𝘁 𝗰𝗼𝗶𝗻𝘀:  {data[idtg]["dop2"]["events_coin"]}💰
                ''',  reply_markup=markup)
                bot.register_next_step_handler(message, events_shop)
            def otpr(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Send🛫')
                    btn2 = types.KeyboardButton('Bank🏛')
                    btn3 = types.KeyboardButton('Get🛬')
                    btn4 = types.KeyboardButton('Top by balance🏆')
                    btn5 = types.KeyboardButton('Profile🙍‍♂')
                    btn6 = types.KeyboardButton('Top by referrals🏆')
                    btn7 = types.KeyboardButton('Events👾')
                    btn8 = types.KeyboardButton('Services📚')
                    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
                    bot.send_message(message.chat.id, f'''
                        𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

                𝗡𝗮𝗺𝗲: {data[idtg]["name"]}🙍‍♂
                𝗘𝗺𝗮𝗶𝗹:  {data[idtg]["email"]}
                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                
                𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    #перевод человека
                    bot.register_next_step_handler(message, wallet)
                else:
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    mes = message.text
                    bot.send_message(message.chat.id, f'Amount:',  reply_markup=markup)
                    bot.register_next_step_handler(message, otpr1, mes)
            def otpr1(message, mes):
                
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Send🛫')
                    btn2 = types.KeyboardButton('Bank🏛')
                    btn3 = types.KeyboardButton('Get🛬')
                    btn4 = types.KeyboardButton('Top by balance🏆')
                    btn5 = types.KeyboardButton('Profile🙍‍♂')
                    btn6 = types.KeyboardButton('Top by referrals🏆')
                    btn7 = types.KeyboardButton('Events👾')
                    btn8 = types.KeyboardButton('Services📚')
                    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
                    bot.send_message(message.chat.id, f'''
                        𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

                𝗡𝗮𝗺𝗲: {data[idtg]["name"]}🙍‍♂
                𝗘𝗺𝗮𝗶𝗹:  {data[idtg]["email"]}
                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                
                𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    #перевод человека
                    bot.register_next_step_handler(message, wallet)
                else:
                    try:
                        if mes == data[idtg]["token"]:
                            bot.send_message(message.chat.id, f'There is no such token!\nWrite the token of the wallet to which you want to make the transfer:')
                            bot.register_next_step_handler(message,otpr)

                        elif data[idtg]["tgcoins"] >= int(message.text):
                            for i in data:
                                m = " "
                                if mes == data[i]["token"]:
                                
                                    pol1 = data[idtg]["tgcoins"] - int(message.text)
                                    pol2 = data[i]["tgcoins"] + int(message.text)
                                    data[idtg]["tgcoins"] = pol1
                                    data[i]["tgcoins"] = pol2
                                    with open('bd_telebot.json', 'w') as file:
                                        json.dump(data, file, indent=4)
                                    bot.send_message(i, f'You have been transferred: {message.text} Telecoins!')
                                    bot.send_message(message.chat.id, f'The transfer was successfully made✅')
                                    m = "Кошелек"
                                    bot.register_next_step_handler(message, start)
                                    break
                            if m != "Кошелек":
                                bot.send_message(message.chat.id, f'There is no such token!\nWrite the token of the wallet to which you want to make the transfer:')
                                bot.register_next_step_handler(message,otpr)
                        else:

                            bot.send_message(message.chat.id, f'There is no such amount on the balance sheet\nAmount:')
                            bot.register_next_step_handler(message,otpr1,mes )
                    except:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        bot.send_message(message.chat.id, f'An error has occurred! Most likely you entered the wrong amount instead of the amount you need)\nTry again!\n',  reply_markup=markup)
                        bot.register_next_step_handler(message, start)




            def bank(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Send🛫')
                    btn2 = types.KeyboardButton('Bank🏛')
                    btn3 = types.KeyboardButton('Get🛬')
                    btn4 = types.KeyboardButton('Top by balance🏆')
                    btn5 = types.KeyboardButton('Profile🙍‍♂')
                    btn6 = types.KeyboardButton('Top by referrals🏆')
                    btn7 = types.KeyboardButton('Events👾')
                    btn8 = types.KeyboardButton('Services📚')
                    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
                    bot.send_message(message.chat.id, f'''
                        𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

                𝗡𝗮𝗺𝗲: {data[idtg]["name"]}🙍‍♂
                𝗘𝗺𝗮𝗶𝗹:  {data[idtg]["email"]}
                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                
                𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    #перевод человека
                    bot.register_next_step_handler(message, wallet)
                elif message.text == 'Replenish📥':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    
                    bot.send_message(message.chat.id, f'Amount:',  reply_markup=markup)
                    bot.register_next_step_handler(message, bank_rep)
                elif message.text == 'Bring out📤':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    
                    bot.send_message(message.chat.id, f'Amount:',  reply_markup=markup)
                    bot.register_next_step_handler(message, bank_br)
                elif message.text == 'Receive %':
                    t = time.time()
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    if t - data[idtg]["dop2"]["bank_time"] >= 84000:
                        random.randint(1, 4)
                        if random.randint(1, 4) <= 3:
                            q = time.time()
                            e = data[idtg]["power"] * 0.01
                            pol = data[idtg]["dop2"]["bank"] * e
                            print(pol, e)
                            b = data[idtg]["dop2"]["bank"] + round(pol)
                            data[idtg]["dop2"]["bank"] = b
                            data[idtg]["dop2"]["bank_time"] = q
                            with open('bd_telebot.json', 'w') as file:
                                json.dump(data, file, indent=4)
                            reply_markup = types.ReplyKeyboardRemove()
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                            btn1 = types.KeyboardButton('Back👈🏻')
                            markup.add(btn1)
                            bot.send_message(message.chat.id, f'Interest received successfully!✅',  reply_markup=markup)
                            bot.register_next_step_handler(message, backbank)
                        else:
                            with open('bd_telebot.json', 'r') as file:
                                data = json.load(file)
                            idtg = str(message.from_user.id)
                            q = time.time()
                            data[idtg]["dop2"]["bank_time"] = q
                            with open('bd_telebot.json', 'w') as file:
                                json.dump(data, file, indent=4)
                            reply_markup = types.ReplyKeyboardRemove()
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                            btn1 = types.KeyboardButton('Back👈🏻')
                            markup.add(btn1)
                            bot.send_message(message.chat.id, f'Unfortunately, the bank refused to pay interest💰\nCome back tomorrow!',  reply_markup=markup)
                            bot.register_next_step_handler(message, backbank)
                    else:
                        reply_markup = types.ReplyKeyboardRemove()
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f"Mistake! It hasn't been day yet!❌",  reply_markup=markup)
                        bot.register_next_step_handler(message, backbank)
                elif message.text == 'Investment📜':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton("Buy Coins👛")
                    btn2 = types.KeyboardButton('Portfolio💼')
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                        𝗜𝗻𝘃𝗲𝘀𝘁𝗺𝗲𝗻𝘁📜

                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                
                𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    #перевод человека
                    bot.register_next_step_handler(message, invest)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    bot.send_message(message.chat.id, f'An error has occurred! Try again!',  reply_markup=markup)
                    bot.register_next_step_handler(message, backbank)
            def invest(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Replenish📥')
                    btn2 = types.KeyboardButton('Receive %')
                    btn22 = types.KeyboardButton('Bring out📤')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn22, btn7)
                    bot.send_message(message.chat.id, f'''
                    𝗕𝗮𝗻𝗸🏛

                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                𝗜𝗻 𝘁𝗵𝗲 𝗕𝗮𝗻𝗸: {data[idtg]["dop2"]["bank"]}🏛
                𝗣𝗲𝗿𝗰𝗲𝗻𝘁𝗮𝗴𝗲𝘀: {data[idtg]["power"]}%
                
                𝗖𝗵𝗼𝗼𝘀𝗲 𝘄𝗵𝗮𝘁 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼👇🏻

                
                        ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, bank)
                elif message.text == 'Buy Coins👛':
                    ac_e = yahooFinance.Ticker("ETH-USD")
                    ac_b = yahooFinance.Ticker("BTC-USD")
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Bitcoin')
                    btn2 = types.KeyboardButton('Ethereum')
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                    𝗕𝘂𝘆 𝗖𝗼𝗶𝗻𝘀👛

                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                
                𝗕𝗶𝘁𝗰𝗼𝗶𝗻: {ac_b.info['regularMarketPrice']} 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻𝘀
                𝗘𝘁𝗵𝗲𝗿𝗲𝘂𝗺: {ac_e.info['regularMarketPrice']} 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻𝘀
                
                𝗖𝗵𝗼𝗼𝘀𝗲 𝘄𝗵𝗶𝗰𝗵 𝗰𝘂𝗿𝗿𝗲𝗻𝗰𝘆 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗯𝘂𝘆 𝗼𝗿 𝘀𝗲𝗹𝗹👇🏻

                
                        ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, bc)
                elif message.text == 'Portfolio💼':
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    𝗣𝗼𝗿𝘁𝗳𝗼𝗹𝗶𝗼💼
                𝗜𝗻 𝘆𝗼𝘂𝗿 𝗽𝗼𝗿𝘁𝗳𝗼𝗹𝗶𝗼 𝗶𝘀:

                𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻𝘀:  {data[idtg]["tgcoins"]}
                𝗕𝗶𝘁𝗰𝗼𝗶𝗻𝘀: {data[idtg]["dop2"]["bank_ac"]["btc"]} 
                𝗘𝘁𝗵𝗲𝗿𝗲𝘂𝗺𝘀: {data[idtg]["dop2"]["bank_ac"]["eth"]} 
                
                𝗖𝗵𝗼𝗼𝘀𝗲 𝘄𝗵𝗮𝘁 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼👇🏻

                
                        ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, backinv)
            def bc(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton("Buy Coins👛")
                    btn2 = types.KeyboardButton('Portfolio💼')
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                        𝗜𝗻𝘃𝗲𝘀𝘁𝗺𝗲𝗻𝘁📜

                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                
                𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    #перевод человека
                    bot.register_next_step_handler(message, invest)
                if message.text == 'Bitcoin':
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    ac_e = yahooFinance.Ticker("ETH-USD")
                    ac_b = yahooFinance.Ticker("BTC-USD")
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    𝗕𝗶𝘁𝗰𝗼𝗶𝗻
                𝗦𝘁𝗮𝘁𝗶𝘀𝘁𝗶𝗰𝘀:

                1 𝗕𝗶𝘁𝗰𝗼𝗶𝗻𝘀 = {round(ac_b.info['regularMarketPrice'])} 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻𝘀
                
                𝗠𝗶𝗻𝗶𝗺𝘂𝗺 𝗽𝗿𝗶𝗰𝗲 𝗳𝗼𝗿 𝘁𝗼𝗱𝗮𝘆: {round(ac_b.info['dayLow'])} 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻𝘀
                𝗠𝗮𝘅𝗶𝗺𝘂𝗺 𝗽𝗿𝗶𝗰𝗲 𝗳𝗼𝗿 𝘁𝗼𝗱𝗮𝘆: {round(ac_b.info['dayHigh'])} 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻𝘀
                𝗖𝗵𝗼𝗼𝘀𝗲 𝘄𝗵𝗮𝘁 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼👇🏻

                
                        ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, backinv)
            def bank_br(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Replenish📥')
                    btn2 = types.KeyboardButton('Receive %')
                    btn22 = types.KeyboardButton('Bring out📤')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn22, btn7)
                    bot.send_message(message.chat.id, f'''
                    𝗕𝗮𝗻𝗸🏛

                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                𝗜𝗻 𝘁𝗵𝗲 𝗕𝗮𝗻𝗸: {data[idtg]["dop2"]["bank"]}🏛
                𝗣𝗲𝗿𝗰𝗲𝗻𝘁𝗮𝗴𝗲𝘀: {data[idtg]["power"]}%
                
                𝗖𝗵𝗼𝗼𝘀𝗲 𝘄𝗵𝗮𝘁 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼👇🏻

                
                        ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, bank)
                else:
                    try:
                        if data[idtg]["dop2"]["bank"] >= int(message.text):
                            pol1 = data[idtg]["tgcoins"] + int(message.text)
                            pol2 = data[idtg]["dop2"]["bank"] - int(message.text)
                            data[idtg]["tgcoins"] = pol1
                            data[idtg]["dop2"]["bank"] = pol2
                            with open('bd_telebot.json', 'w') as file:
                                json.dump(data, file, indent=4)
                            bot.send_message(message.chat.id, f'The transfer was successfully made✅')
                            bot.register_next_step_handler(message, backbank)
                        else:

                            bot.send_message(message.chat.id, f'There is no such amount on the balance sheet\nAmount:')
                            bot.register_next_step_handler(message, bank_br)
                    except:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        bot.send_message(message.chat.id, f'An error has occurred! Most likely you entered the wrong amount instead of the amount you need)\nTry again!\n',  reply_markup=markup)
                        bot.register_next_step_handler(message,  backbank)
            def bank_rep(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Replenish📥')
                    btn2 = types.KeyboardButton('Receive %')
                    btn22 = types.KeyboardButton('Bring out📤')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn22, btn7)
                    bot.send_message(message.chat.id, f'''
                    𝗕𝗮𝗻𝗸🏛

                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                𝗜𝗻 𝘁𝗵𝗲 𝗕𝗮𝗻𝗸: {data[idtg]["dop2"]["bank"]}🏛
                𝗣𝗲𝗿𝗰𝗲𝗻𝘁𝗮𝗴𝗲𝘀: {data[idtg]["power"]}%
                
                𝗖𝗵𝗼𝗼𝘀𝗲 𝘄𝗵𝗮𝘁 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼👇🏻

                
                        ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, bank)
                else:
                    try:
                        if data[idtg]["tgcoins"] >= int(message.text):
                            pol1 = data[idtg]["tgcoins"] - int(message.text)
                            pol2 = data[idtg]["dop2"]["bank"] + int(message.text)
                            data[idtg]["tgcoins"] = pol1
                            data[idtg]["dop2"]["bank"] = pol2
                            with open('bd_telebot.json', 'w') as file:
                                json.dump(data, file, indent=4)
                            bot.send_message(message.chat.id, f'The transfer was successfully made✅')
                            bot.register_next_step_handler(message,  backbank)
                        else:

                            bot.send_message(message.chat.id, f'There is no such amount on the balance sheet\nAmount:')
                            bot.register_next_step_handler(message, bank_rep)
                    except:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        bot.send_message(message.chat.id, f'An error has occurred! Most likely you entered the wrong amount instead of the amount you need)\nTry again!\n',  reply_markup=markup)
                        bot.register_next_step_handler(message,  backbank)
            def backbank(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                reply_markup = types.ReplyKeyboardRemove()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                btn1 = types.KeyboardButton('Replenish📥')
                btn2 = types.KeyboardButton('Receive %')
                btn22 = types.KeyboardButton('Bring out📤')
                btn7 = types.KeyboardButton('Back👈🏻')
                markup.add(btn1, btn2, btn22, btn7)
                bot.send_message(message.chat.id, f'''
                𝗕𝗮𝗻𝗸🏛

            𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
            𝗜𝗻 𝘁𝗵𝗲 𝗕𝗮𝗻𝗸: {data[idtg]["dop2"]["bank"]}🏛
            𝗣𝗲𝗿𝗰𝗲𝗻𝘁𝗮𝗴𝗲𝘀: {data[idtg]["power"]}%
            
            𝗖𝗵𝗼𝗼𝘀𝗲 𝘄𝗵𝗮𝘁 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼👇🏻

            
                    ''',  reply_markup=markup)
                bot.register_next_step_handler(message, bank)




            def prof(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Send🛫')
                    btn2 = types.KeyboardButton('Bank🏛')
                    btn3 = types.KeyboardButton('Get🛬')
                    btn4 = types.KeyboardButton('Top by balance🏆')
                    btn5 = types.KeyboardButton('Profile🙍‍♂')
                    btn6 = types.KeyboardButton('Top by referrals🏆')
                    btn7 = types.KeyboardButton('Events👾')
                    btn8 = types.KeyboardButton('Services📚')
                    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
                    bot.send_message(message.chat.id, f'''
                        𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

                𝗡𝗮𝗺𝗲: {data[idtg]["name"]}🙍‍♂
                𝗘𝗺𝗮𝗶𝗹:  {data[idtg]["email"]}
                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                
                𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    #перевод человека
                    bot.register_next_step_handler(message, wallet)
                else:
                    if message.text == 'Change Email':
                        reply_markup = types.ReplyKeyboardRemove()
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'Specify Email:',  reply_markup=markup)
                        bot.register_next_step_handler(message, email)
                    elif message.text == 'Change Nickname':
                    
                        reply_markup = types.ReplyKeyboardRemove()
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'Specify Nickname (maximum of 8 characters):',  reply_markup=markup)
                        bot.register_next_step_handler(message, nick)
                    elif message.text == 'Referral program':
                        with open('bd_telebot.json', 'r') as file:
                            data = json.load(file)
                        idtg = str(message.from_user.id)
                        if "reffer" not in data[idtg]["dop2"]:
                            
                            data[idtg]["dop2"]["reffer"] = []
                            with open('bd_telebot.json', 'w') as file:
                                json.dump(data, file, indent=4)
                        if "ref_total" not in data[idtg]["dop2"]:
                            data[idtg]["dop2"]["ref_token"] = 0
                            with open('bd_telebot.json', 'w') as file:
                                json.dump(data, file, indent=4)

                        reply_markup = types.ReplyKeyboardRemove()
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
    𝗥𝗲𝗳𝗲𝗿𝗿𝗮𝗹 𝗽𝗿𝗼𝗴𝗿𝗮𝗺

Total people: {len(data[idtg]["dop2"]["reffer"])}

Your referral link: <code>{"https://t.me/textobnjvqbot?start="+idtg}</code>
                
For 1 referral you will receive 300 Telecoins and 0.5% in bank!

And the referral will receive 300 Telecoins!
                        ''',  reply_markup=markup, parse_mode='HTML' )
                        bot.register_next_step_handler(message, backp)
                    elif message.text == 'Subscription':
                        reply_markup = types.ReplyKeyboardRemove()
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Buy❌')
                        btn2 = types.KeyboardButton('Back👈🏻')
                        markup.add(btn1, btn2)
                        bot.send_message(message.chat.id, f'''
            Cost - 39 Rubles ✅

Advantages:
- 100% interest withdrawal 🏛
- x2 interest in the bank 🏛
- x2 referral bonus 🎁

Conditions:
- Subscription is issued for 1 month ✅
- Automatic money transfer is not provided ✅

The first 5 people subscribe forever!🔥

Click and subscribe 👇
            
                        ''',  reply_markup=markup)
                        bot.register_next_step_handler(message, sub)
                    else:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        bot.send_message(message.chat.id, f'An error has occurred! Try again!',  reply_markup=markup)
                        bot.register_next_step_handler(message, backp)
            def sub(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Change Email')
                    btn2 = types.KeyboardButton('Change Nickname')
                    btn3 = types.KeyboardButton('Referral program')
                    btn4 = types.KeyboardButton('Subscription')
                    btn5 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    n = '\n'
                    bot.send_message(message.chat.id, f'''
                𝗣𝗿𝗼𝗳𝗶𝗹𝗲🙍‍♂
𝗡𝗮𝗺𝗲: {data[idtg]["name"]}🙍‍♂
𝗘𝗺𝗮𝗶𝗹:  {data[idtg]["email"]}
𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻: {data[idtg]["dop2"]["sub"]}
𝗠𝗲𝗱𝗮𝗹𝘀: 
{n.join(data[idtg]["dop2"]["med"])}

𝗪𝗵𝗮𝘁 𝗱𝗼 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼?
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, prof)
                if message.text == "Buy✅":
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Check payment🔄')
                    btn2 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
            Buy✅
        To purchase, follow the link, write the amount and your ID in the message! 

        Cost = 39 rub

        ID - <code>{idtg}</code>

        Link: https://vk.com/public216185000?w=app6887721_-216185000

        If you have any questions about the purchase, go here:https://vk.com/topic-216185000_49417086

                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, sub_pro)
                else:
                    
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'Subscription purchase is not available yet... Wait for news!',  reply_markup=markup)
                    bot.register_next_step_handler(message, backp)
            def sub_pro(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Buy✅')
                    btn2 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
        Cost - 39 Rubles ✅

Advantages:
- 100% interest withdrawal 🏛
- x2 interest in the bank 🏛
- x2 referral bonus 🎁

Conditions:
- Subscription is issued for 1 month ✅
- Automatic money transfer is not provided ✅

The first 5 people subscribe forever!🔥

Click and subscribe 👇
        
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, sub)
                else:
                    
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'Subscription purchase is not available yet... Wait for news!',  reply_markup=markup)
                    bot.register_next_step_handler(message, backp)
            def email(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Change Email')
                    btn2 = types.KeyboardButton('Change Nickname')
                    btn3 = types.KeyboardButton('Referral program')
                    btn4 = types.KeyboardButton('Subscription')
                    btn5 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(message.chat.id, f'''
                𝗣𝗿𝗼𝗳𝗶𝗹𝗲🙍‍♂
            𝗡𝗮𝗺𝗲: {data[idtg]["name"]}🙍‍♂
            𝗘𝗺𝗮𝗶𝗹:  {data[idtg]["email"]}
            𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻: ❌
            𝗪𝗵𝗮𝘁 𝗱𝗼 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼?
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, prof)
                else:
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    data[idtg]["email"] = message.text
                    with open('bd_telebot.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'The change was made successfully!✅',  reply_markup=markup)
                    bot.register_next_step_handler(message, backp)
            def nick(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Change Email')
                    btn2 = types.KeyboardButton('Change Nickname')
                    btn3 = types.KeyboardButton('Referral program')
                    btn4 = types.KeyboardButton('Subscription')
                    btn5 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(message.chat.id, f'''
                𝗣𝗿𝗼𝗳𝗶𝗹𝗲🙍‍♂
            𝗡𝗮𝗺𝗲: {data[idtg]["name"]}🙍‍♂
            𝗘𝗺𝗮𝗶𝗹:  {data[idtg]["email"]}
            𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻: ❌
            𝗪𝗵𝗮𝘁 𝗱𝗼 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼?
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, prof)
                elif len(message.text) <= 8:
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    data[idtg]["name"] = message.text
                    with open('bd_telebot.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'The change was made successfully!✅',  reply_markup=markup)
                    bot.register_next_step_handler(message, backp)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'You have specified a nickname that is more than 8 characters! Try again!',  reply_markup=markup)
                    bot.register_next_step_handler(message, backp)
            def backp(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                
                reply_markup = types.ReplyKeyboardRemove()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                btn1 = types.KeyboardButton('Change Email')
                btn2 = types.KeyboardButton('Change Nickname')
                btn3 = types.KeyboardButton('Referral program')
                btn4 = types.KeyboardButton('Subscription')
                btn5 = types.KeyboardButton('Back👈🏻')
                markup.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(message.chat.id, f'''
            𝗣𝗿𝗼𝗳𝗶𝗹𝗲🙍‍♂
        𝗡𝗮𝗺𝗲: {data[idtg]["name"]}🙍‍♂
        𝗘𝗺𝗮𝗶𝗹:  {data[idtg]["email"]}
        𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻: ❌
        𝗪𝗵𝗮𝘁 𝗱𝗼 𝘆𝗼𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝗱𝗼?
                ''',  reply_markup=markup)
                bot.register_next_step_handler(message, prof)


            def serv(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Send🛫')
                    btn2 = types.KeyboardButton('Bank🏛')
                    btn3 = types.KeyboardButton('Get🛬')
                    btn4 = types.KeyboardButton('Top by balance🏆')
                    btn5 = types.KeyboardButton('Profile🙍‍♂')
                    btn6 = types.KeyboardButton('Top by referrals🏆')
                    btn7 = types.KeyboardButton('Events👾')
                    btn8 = types.KeyboardButton('Services📚')
                    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
                    bot.send_message(message.chat.id, f'''
                        𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

                𝗡𝗮𝗺𝗲: {data[idtg]["name"]}🙍‍♂
                𝗘𝗺𝗮𝗶𝗹:  {data[idtg]["email"]}
                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                
                𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    #перевод человека
                    bot.register_next_step_handler(message, wallet)
                elif message.text == 'The development team/website':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'𝗢𝘂𝗿 𝗩𝗞 𝗚𝗿𝗼𝘂𝗽:https://vk.com/the.telecoin\n𝗢𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻 𝗪𝗲𝗯𝘀𝗶𝘁𝗲:(In development...)',  reply_markup=markup)
                    bot.register_next_step_handler(message, backs)
                elif message.text == 'TeleShop':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Buy Telecoins💳')
                    btn2 = types.KeyboardButton('Exchange Telecoins🔄')
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'𝗛𝗲𝗿𝗲 𝘄𝗲 𝗰𝗮𝗻 𝗯𝘂𝘆, 𝗲𝘅𝗰𝗵𝗮𝗻𝗴𝗲 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻𝘀\n𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻',  reply_markup=markup)
                    bot.register_next_step_handler(message, teleshop)
                elif message.text == 'TeleGame':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Heads and Tails💰')
                    btn2 = types.KeyboardButton('Shooting gallery🔫')
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'Choose a game👇🏻',  reply_markup=markup)
                    bot.register_next_step_handler(message, game)
                elif message.text == 'TeleStats':
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    k = data.keys()
                    f = 0
                    q = 0
                    for k in data:
                        try:
                            f += data[k]["tgcoins"] + data[k]["dop2"]["bank"]
                            
                        except:
                            f += data[k]["tgcoins"]
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    𝗧𝗲𝗹𝗲𝗦𝘁𝗮𝘁𝘀

                Total people: {len(data)}🙍‍♂
                Total Telecoins: {f}💰
                
                𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    #перевод человека
                    bot.register_next_step_handler(message, backs)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    bot.send_message(message.chat.id, f'An error has occurred! Try again!',  reply_markup=markup)
                    bot.register_next_step_handler(message, backs)
            def game(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('TeleShop')
                    btn2 = types.KeyboardButton('TeleGame')
                    btn22 = types.KeyboardButton('TeleStats')
                    btn3 = types.KeyboardButton('The development team/website')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn22, btn3, btn7)
                    bot.send_message(message.chat.id, f'''
                    𝗧𝗵𝗲𝘀𝗲 𝗮𝗿𝗲 𝗮𝗹𝗹 𝗼𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻 𝘀𝗲𝗿𝘃𝗶𝗰𝗲𝘀! 
                    𝗦𝗲𝗹𝗲𝗰𝘁 𝗼𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝗺 𝗼𝗿 𝗿𝗲𝘁𝘂𝗿𝗻 𝘁𝗼 𝘁𝗵𝗲 𝗺𝗲𝗻𝘂)
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, serv)
                elif message.text == 'Heads and Tails💰':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Eagle🦅')
                    btn2 = types.KeyboardButton('Tails🎱')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn7)
                    bot.send_message(message.chat.id, f'  𝗛𝗲𝗮𝗱𝘀 𝗮𝗻𝗱 𝗧𝗮𝗶𝗹𝘀💰\n   𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰\n\n𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻', reply_markup=markup)
                    bot.register_next_step_handler(message, hor_stawka)
                elif message.text == 'Shooting gallery🔫':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Play🔫')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn7)
                    bot.send_message(message.chat.id, f'  𝙎𝙝𝙤𝙤𝙩𝙞𝙣𝙜 𝙜𝙖𝙡𝙡𝙚𝙧𝙮🔫\n   𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰\n\n𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻', reply_markup=markup)
                    bot.register_next_step_handler(message, tir_stawka)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    bot.send_message(message.chat.id, f'An error has occurred! Try again!',  reply_markup=markup)
                    bot.register_next_step_handler(message, backs)


            def hor_stawka(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('TeleShop')
                    btn2 = types.KeyboardButton('TeleGame')
                    btn22 = types.KeyboardButton('TeleStats')
                    btn3 = types.KeyboardButton('The development team/website')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn22, btn3, btn7)
                    bot.send_message(message.chat.id, f'''
                    𝗧𝗵𝗲𝘀𝗲 𝗮𝗿𝗲 𝗮𝗹𝗹 𝗼𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻 𝘀𝗲𝗿𝘃𝗶𝗰𝗲𝘀! 
                    𝗦𝗲𝗹𝗲𝗰𝘁 𝗼𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝗺 𝗼𝗿 𝗿𝗲𝘁𝘂𝗿𝗻 𝘁𝗼 𝘁𝗵𝗲 𝗺𝗲𝗻𝘂)
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, serv)
                elif message.text == 'Eagle🦅' or message.text == 'Tails🎱':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'Specify the bid:',  reply_markup=markup)
                    bot.register_next_step_handler(message, hor)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'An error has occurred! Try again!',  reply_markup=markup)
                    bot.register_next_step_handler(message, backs)
            def hor(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Eagle🦅')
                    btn2 = types.KeyboardButton('Tails🎱')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn7)
                    bot.send_message(message.chat.id, f'  𝗛𝗲𝗮𝗱𝘀 𝗮𝗻𝗱 𝗧𝗮𝗶𝗹𝘀💰\n𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰\n\n𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻', reply_markup=markup)
                    bot.register_next_step_handler(message, hor_stawka)
                else:
                    try:
                        with open('bd_telebot.json', 'r') as file:
                            data = json.load(file)
                        idtg = str(message.from_user.id)
                        if data[idtg]["tgcoins"] >= int(message.text):
                            res = random.randint(1, 2)
                            
                            if res == 1:
                                
                                x2 = int(message.text) * 2
                                pol1 = data[idtg]["tgcoins"] + int(message.text)
                                data[idtg]["tgcoins"] = pol1
                                with open('bd_telebot.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                                reply_markup = types.ReplyKeyboardRemove()
                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                                btn2 = types.KeyboardButton('Back👈🏻')
                                markup.add(btn2)
                                bot.send_message(message.chat.id, f"You've won! You received: {x2} Telecoins✅",  reply_markup=markup)
                                bot.register_next_step_handler(message, backhor)
                            else:
                                
                                pol1 = data[idtg]["tgcoins"] - int(message.text)
                                data[idtg]["tgcoins"] = pol1
                                with open('bd_telebot.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                                reply_markup = types.ReplyKeyboardRemove()
                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                                btn2 = types.KeyboardButton('Back👈🏻')
                                markup.add(btn2)
                                bot.send_message(message.chat.id, f"Unfortunately you lost: {message.text} Telecoins...",  reply_markup=markup)
                                bot.register_next_step_handler(message, backhor)
                        else:

                            reply_markup = types.ReplyKeyboardRemove()
                            btn2 = types.KeyboardButton('Back👈🏻')
                            markup.add(btn2)
                            bot.send_message(message.chat.id, f"You don't have enough coins to bet) Try to specify a different bid!",  reply_markup=markup)
                            bot.register_next_step_handler(message, backhor)
                    except:
                        reply_markup = types.ReplyKeyboardRemove()
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'An error has occurred! Try again!',  reply_markup=markup)
                        bot.register_next_step_handler(message, backhor)
            def tir_stawka(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('TeleShop')
                    btn2 = types.KeyboardButton('TeleGame')
                    btn22 = types.KeyboardButton('TeleStats')
                    btn3 = types.KeyboardButton('The development team/website')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn22, btn3, btn7)
                    bot.send_message(message.chat.id, f'''
                    𝗧𝗵𝗲𝘀𝗲 𝗮𝗿𝗲 𝗮𝗹𝗹 𝗼𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻 𝘀𝗲𝗿𝘃𝗶𝗰𝗲𝘀! 
                    𝗦𝗲𝗹𝗲𝗰𝘁 𝗼𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝗺 𝗼𝗿 𝗿𝗲𝘁𝘂𝗿𝗻 𝘁𝗼 𝘁𝗵𝗲 𝗺𝗲𝗻𝘂)
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, serv)
                elif message.text == 'Play🔫':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'Specify the bid:',  reply_markup=markup)
                    bot.register_next_step_handler(message, tir)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'An error has occurred! Try again!',  reply_markup=markup)
                    bot.register_next_step_handler(message, backs)
            def tir(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Play🔫')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn7)
                    bot.send_message(message.chat.id, f'  𝙎𝙝𝙤𝙤𝙩𝙞𝙣𝙜 𝙜𝙖𝙡𝙡𝙚𝙧𝙮🔫\n   𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰\n\n𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻', reply_markup=markup)
                    bot.register_next_step_handler(message, tir_stawka)
                else:
                    try:
                        with open('bd_telebot.json', 'r') as file:
                            data = json.load(file)
                        idtg = str(message.from_user.id)
                        if data[idtg]["tgcoins"] >= int(message.text):
                            t = bot.send_dice(message.chat.id, f'🎯')
                            
                            for i in range(1, 10000000):
                                r = 1
                            if int(t.dice.value) == 6:
                                x3 = int(message.text) * 3
                                pol1 = data[idtg]["tgcoins"] + int(message.text) * 2
                                data[idtg]["tgcoins"] = pol1
                                with open('bd_telebot.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                                reply_markup = types.ReplyKeyboardRemove()
                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                                btn2 = types.KeyboardButton('Back👈🏻')
                                markup.add(btn2)
                                bot.send_message(message.chat.id, f"You've won! You received: {x3} Telecoins✅",  reply_markup=markup)
                                bot.register_next_step_handler(message, backtir)
                            elif int(t.dice.value) == 5:
                                x2 = int(message.text) * 2
                                pol1 = data[idtg]["tgcoins"] + int(message.text)
                                data[idtg]["tgcoins"] = pol1
                                with open('bd_telebot.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                                reply_markup = types.ReplyKeyboardRemove()
                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                                btn2 = types.KeyboardButton('Back👈🏻')
                                markup.add(btn2)
                                bot.send_message(message.chat.id, f"You've won! You received: {x2} Telecoins✅",  reply_markup=markup)
                                bot.register_next_step_handler(message, backtir)
                            elif int(t.dice.value) == 4:
                                x1 = int(message.text) 
                                pol1 = data[idtg]["tgcoins"]
                                data[idtg]["tgcoins"] = pol1
                                with open('bd_telebot.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                                reply_markup = types.ReplyKeyboardRemove()
                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                                btn2 = types.KeyboardButton('Back👈🏻')
                                markup.add(btn2)
                                bot.send_message(message.chat.id, f"You've won! You received: {x1} Telecoins✅",  reply_markup=markup)
                                bot.register_next_step_handler(message, backtir)
                            else:
                                pol1 = data[idtg]["tgcoins"] - int(message.text)
                                data[idtg]["tgcoins"] = pol1
                                with open('bd_telebot.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                                reply_markup = types.ReplyKeyboardRemove()
                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                                btn2 = types.KeyboardButton('Back👈🏻')
                                markup.add(btn2)
                                bot.send_message(message.chat.id, f"Unfortunately you lost: {message.text} Telecoins...",  reply_markup=markup)
                                bot.register_next_step_handler(message, backtir)
                        else:
                            reply_markup = types.ReplyKeyboardRemove()
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                            btn2 = types.KeyboardButton('Back👈🏻')
                            markup.add(btn2)
                            bot.send_message(message.chat.id, f"You don't have enough coins to bet) Try to specify a different bid!",  reply_markup=markup)
                            bot.register_next_step_handler(message, backtir)
                        
                    except:
                        reply_markup = types.ReplyKeyboardRemove()
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Back👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'An error has occurred! Try again!',  reply_markup=markup)
                        bot.register_next_step_handler(message, backtir)
            def backs(message):
                
                
                reply_markup = types.ReplyKeyboardRemove()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                btn1 = types.KeyboardButton('TeleShop')
                btn2 = types.KeyboardButton('TeleGame')
                btn22 = types.KeyboardButton('TeleStats')
                btn3 = types.KeyboardButton('The development team/website')
                btn7 = types.KeyboardButton('Back👈🏻')
                markup.add(btn1, btn2, btn22, btn3, btn7)
                bot.send_message(message.chat.id, f'''
                𝗧𝗵𝗲𝘀𝗲 𝗮𝗿𝗲 𝗮𝗹𝗹 𝗼𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻 𝘀𝗲𝗿𝘃𝗶𝗰𝗲𝘀! 
                𝗦𝗲𝗹𝗲𝗰𝘁 𝗼𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝗺 𝗼𝗿 𝗿𝗲𝘁𝘂𝗿𝗻 𝘁𝗼 𝘁𝗵𝗲 𝗺𝗲𝗻𝘂)
                ''',  reply_markup=markup)
                bot.register_next_step_handler(message, serv)
        
            def backg(message):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                btn1 = types.KeyboardButton('Heads and Tails💰')
                btn2 = types.KeyboardButton('Back👈🏻')
                markup.add(btn1, btn2)
                bot.send_message(message.chat.id, f'Choose a game👇🏻',  reply_markup=markup)
                bot.register_next_step_handler(message, game)
            def backhor(message):
                
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                btn1 = types.KeyboardButton('Eagle🦅')
                btn2 = types.KeyboardButton('Tails🎱')
                btn7 = types.KeyboardButton('Back👈🏻')
                markup.add(btn1, btn2, btn7)
                bot.send_message(message.chat.id, f'  𝗛𝗲𝗮𝗱𝘀 𝗮𝗻𝗱 𝗧𝗮𝗶𝗹𝘀💰\n   𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰\n\n𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻', reply_markup=markup)
                bot.register_next_step_handler(message, hor_stawka)
            def backtir(message):
                
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                reply_markup = types.ReplyKeyboardRemove()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                btn1 = types.KeyboardButton('Play🔫')
                btn7 = types.KeyboardButton('Back👈🏻')
                markup.add(btn1, btn7)
                bot.send_message(message.chat.id, f'  𝙎𝙝𝙤𝙤𝙩𝙞𝙣𝙜 𝙜𝙖𝙡𝙡𝙚𝙧𝙮🔫\n   𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰\n\n𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻', reply_markup=markup)
                bot.register_next_step_handler(message, tir_stawka)
            def admin(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Send🛫')
                    btn2 = types.KeyboardButton('Bank🏛')
                    btn3 = types.KeyboardButton('Get🛬')
                    btn4 = types.KeyboardButton('Top by balance🏆')
                    btn5 = types.KeyboardButton('Profile🙍‍♂')
                    btn6 = types.KeyboardButton('Top by referrals🏆')
                    btn7 = types.KeyboardButton('Events👾')
                    btn8 = types.KeyboardButton('Services📚')
                    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
                    bot.send_message(message.chat.id, f'''
                        𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

                𝗡𝗮𝗺𝗲: {data[idtg]["name"]}🙍‍♂
                𝗘𝗺𝗮𝗶𝗹:  {data[idtg]["email"]}
                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                
                𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    #перевод человека
                    bot.register_next_step_handler(message, wallet)
                    
                elif message.text == 'База данных':
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    k = data.keys()
                    f = 0
                    for k in data:
                        f += data[k]["tgcoins"]
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Полная')
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn3)
                    bot.send_message(message.chat.id, f'''
                    𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

                Всего людей: {len(data)}🙍‍♂
                Всего :  {f}
                𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    #перевод человека
                    bot.register_next_step_handler(message, bd_full)
                elif message.text == 'Рассылка':
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    

                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn3)
                    bot.send_message(message.from_user.id, "Текст:",  reply_markup=markup)
                    bot.register_next_step_handler(message, ras)
                elif message.text == 'Ивенты':
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn3)
                    bot.send_message(message.chat.id, f'''
Дать ивент коины: ec [кошелёк\токен] [сумма]
Дать медаль: m [кошелёк\токен]
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, ivent)
            def ivent(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Send🛫')
                    btn2 = types.KeyboardButton('Bank🏛')
                    btn3 = types.KeyboardButton('Get🛬')
                    btn4 = types.KeyboardButton('Top by balance🏆')
                    btn5 = types.KeyboardButton('Profile🙍‍♂')
                    btn6 = types.KeyboardButton('Top by referrals🏆')
                    btn7 = types.KeyboardButton('Events👾')
                    btn8 = types.KeyboardButton('Services📚')
                    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8)
                    bot.send_message(message.chat.id, f'''
                        𝗜𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻

                𝗡𝗮𝗺𝗲: {data[idtg]["name"]}🙍‍♂
                𝗘𝗺𝗮𝗶𝗹:  {data[idtg]["email"]}
                𝗕𝗮𝗹𝗮𝗻𝗰𝗲:  {data[idtg]["tgcoins"]}💰
                
                𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻
                    ''',  reply_markup=markup)
                    #перевод человека
                    bot.register_next_step_handler(message, wallet)
                else:
                    try:
                        a = message.text.split(" ")
                        if a[0] == "ec":
                            for i in data:
                                if data[i]["token"] == a[1]:
                                    data[i]["dop2"]["events_coin"] = data[i]["dop2"]["events_coin"] + int(a[2])
                                    with open('bd_telebot.json', 'w') as file:
                                        json.dump(data, file, indent=4)
                                    bot.send_message(message.from_user.id, "Готово!")
                                    bot.register_next_step_handler(message, admb)
                        elif a[0] == "m":
                            for i in data:
                                if data[i]["token"] == a[1]:
                                    data[i]["dop2"]["med"].append("🥇𝗛𝗮𝗹𝗹𝗼𝘄𝗲𝗲𝗻 𝗘𝘃𝗲𝗻𝘁 𝟮𝟬𝟮𝟮🎃")
                                    with open('bd_telebot.json', 'w') as file:
                                        json.dump(data, file, indent=4)
                                    bot.send_message(message.from_user.id, "Готово!")
                                    bot.register_next_step_handler(message, admb)
                        else:
                            print(dfsdf)
                    except:
                        bot.send_message(message.from_user.id, "Произошла ошибка!")
                        bot.register_next_step_handler(message, admb)

            def ras(message):
                if message.text == 'Back👈🏻':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('База данных')
                    btn2 = types.KeyboardButton('Рассылка')
                    btn3 = types.KeyboardButton('Ивенты')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3, btn7)
                    bot.send_message(message.chat.id, f'''
                    Админ меню:
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, admin)
                else:
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                
                    k = data.keys()
                
                    for k in data:
                        try:
                            bot.send_message(k, message.text)
                        except :
                            gsd = 1
                        
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn3)
                    bot.send_message(message.from_user.id, "Готово!",  reply_markup=markup)
                    bot.register_next_step_handler(message, admb)
            def bd_full(message):
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                if message.text == 'Back👈🏻':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('База данных')
                    btn2 = types.KeyboardButton('Рассылка')
                    btn3 = types.KeyboardButton('Ивенты')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3, btn7)
                    bot.send_message(message.chat.id, f'''
                    Админ меню:
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, admin)
                else:

                    k = data.keys()
                    pri = ""
                    for k in data:
                        pri = str(k) + " = " + str(data[k])

                        bot.send_message(message.from_user.id, f"{pri}")
                    bot.register_next_step_handler(message, admb)
            def admb(message):
                reply_markup = types.ReplyKeyboardRemove()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                btn1 = types.KeyboardButton('База данных')
                btn2 = types.KeyboardButton('Рассылка')
                btn3 = types.KeyboardButton('Ивенты')
                btn7 = types.KeyboardButton('Back👈🏻')
                markup.add(btn1, btn2, btn3, btn7)
                bot.send_message(message.chat.id, f'''
                Админ меню:
                ''',  reply_markup=markup)
                bot.register_next_step_handler(message, admin)
            def teleshop(message):
                if message.text == 'Back👈🏻':
                    
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('TeleShop')
                    btn2 = types.KeyboardButton('TeleGame')
                    btn22 = types.KeyboardButton('TeleStats')
                    btn3 = types.KeyboardButton('The development team/website')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn22, btn3, btn7)
                    bot.send_message(message.chat.id, f'''
                    𝗧𝗵𝗲𝘀𝗲 𝗮𝗿𝗲 𝗮𝗹𝗹 𝗼𝗳𝗳𝗶𝗰𝗶𝗮𝗹 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻 𝘀𝗲𝗿𝘃𝗶𝗰𝗲𝘀! 
                    𝗦𝗲𝗹𝗲𝗰𝘁 𝗼𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝗺 𝗼𝗿 𝗿𝗲𝘁𝘂𝗿𝗻 𝘁𝗼 𝘁𝗵𝗲 𝗺𝗲𝗻𝘂)
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, serv)
                elif message.text == 'Buy Telecoins💳':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn6 = types.KeyboardButton('Buy Telecoins💳')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn6, btn7)
                    bot.send_message(message.chat.id, f'''
                    Soon there will be a link to the official link to TeleMarket!🔮

                📊Course - 1000000Tc = 1 rub📊

                    
                To buy Telecoin, click on the button below👇
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, telecoinbuy)
                elif message.text == 'Exchange Telecoins🔄':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn6 = types.KeyboardButton('Standoff 2🔫')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn6, btn7)
                    bot.send_message(message.chat.id, f'''
                Choose a game👇
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, shopgame)
                else:
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'An error has occurred! Try again!',  reply_markup=markup)
                    bot.register_next_step_handler(message, shopback)
            def telecoinbuy(message):
                if message.text == 'Back👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Buy Telecoins💳')
                    btn2 = types.KeyboardButton('Exchange Telecoins🔄')
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'𝗛𝗲𝗿𝗲 𝘄𝗲 𝗰𝗮𝗻 𝗯𝘂𝘆, 𝗲𝘅𝗰𝗵𝗮𝗻𝗴𝗲 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻𝘀\n𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻',  reply_markup=markup)
                    bot.register_next_step_handler(message, teleshop)
                elif message.text == 'Buy Telecoins💳' or message.text == 'Check payment🔄':
                    with open('bd_telebot.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Check payment🔄')
                    btn2 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
            Current course

        📊Course - 1000000Tc = 1 rub📊

        To purchase, follow the link, write the amount and your id in the message! The bot itself will automatically send the amount calculated at the current rate!

        ID - <code>{idtg}</code>

        Link: https://vk.com/public216185000?w=app6887721_-216185000

                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, telecoinbuy_pro)
            def telecoinbuy_pro(message):
                apikey = "bff7ed3ca6510d2af385f7963f81eedd2accd04a27a0cd6a4d"
                group_id = 216185000
                keksik_api = KeksikApi(group_id, apikey)
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Buy Telecoins💳')
                    btn2 = types.KeyboardButton('Exchange Telecoins🔄')
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'𝗛𝗲𝗿𝗲 𝘄𝗲 𝗰𝗮𝗻 𝗯𝘂𝘆, 𝗲𝘅𝗰𝗵𝗮𝗻𝗴𝗲 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻𝘀\n𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻',  reply_markup=markup)
                    bot.register_next_step_handler(message, teleshop)
                elif message.text == 'Buy Telecoins💳' or message.text == 'Check payment🔄':
                    t = keksik_api.donates.get()
                    print(t)
                    tlen = len(t)
                    print(tlen)
                    for i in (0, tlen - 1):
                        if t[i].msg == idtg:
                            if t[i].date not in data[idtg]["dop1"]:
                                sum = int(t[i].amount) * 1000000

                                pol1 = data[idtg]["tgcoins"] + int(sum)
                                data[idtg]["dop1"].append(t[i].date)
                                data[idtg]["tgcoins"] = pol1
                                with open('bd_telebot.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                                btn3 = types.KeyboardButton('Back👈🏻')
                                markup.add(btn3)
                                bot.send_message(message.chat.id, f'The transfer came to {sum} Telecoins!✅',  reply_markup=markup)
                                
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Check payment🔄')
                    btn2 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
            Current course

        📊Course - 1000000Tc = 1 rub📊

        To purchase, follow the link, write the amount and your id in the message! The bot itself will automatically send the amount calculated at the current rate!

        ID - <code>{idtg}</code>

        Link: https://vk.com/public216185000?w=app6887721_-216185000

                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, telecoinbuy)

            def shopgame(message):
                if message.text == 'Back👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Buy Telecoins💳')
                    btn2 = types.KeyboardButton('Exchange Telecoins🔄')
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'𝗛𝗲𝗿𝗲 𝘄𝗲 𝗰𝗮𝗻 𝗯𝘂𝘆, 𝗲𝘅𝗰𝗵𝗮𝗻𝗴𝗲 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻𝘀\n𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻',  reply_markup=markup)
                    bot.register_next_step_handler(message, teleshop)
                elif message.text == 'Standoff 2🔫':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('10 Gold🍯')
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn3)
                    bot.send_message(message.chat.id, f'''
Here you can exchange Telecoins for gold in Standoff 2🍯

This function is introduced in test mode!💻

Choose a product👇
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, shopgold)
                else:
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'An error has occurred! Try again!',  reply_markup=markup)
                    bot.register_next_step_handler(message, shopgameback)
            def shopgold(message):
                with open('sis.json', 'r') as file:
                    data = json.load(file)
                if message.text == 'Back👈🏻':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn6 = types.KeyboardButton('Standoff 2🔫')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn6, btn7)
                    bot.send_message(message.chat.id, f'''
                Choose a game👇
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, shopgame)
                elif message.text == '10 Gold🍯':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn6 = types.KeyboardButton('Buy')
                    btn7 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn6, btn7)
                    bot.send_message(message.chat.id, f'''
10 Gold🍯

Cost: 1000 Telecoins💰

Seller: Telecoin - Coin in Telegram🙍

Quantity: {data["shop"]["standoff"]["gold10"]["quant"]}
                
1 user - 1 product

❗After the purchase, you will receive a special code that you will need to send to the seller, after which he will tell you how you can get your goods❗

Select the button👇
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, shopgold10)
                else:
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'An error has occurred! Try again!',  reply_markup=markup)
                    bot.register_next_step_handler(message, shopgoldback)
            def shopgold10(message):
                with open('sis.json', 'r') as file:
                    sis = json.load(file)
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Back👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('10 Gold🍯')
                    btn3 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1, btn3)
                    bot.send_message(message.chat.id, f'''
Here you can exchange Telecoins for gold in Standoff 2🍯

This function is introduced in test mode!💻

Choose a product👇
                    ''',  reply_markup=markup)
                    bot.register_next_step_handler(message, shopgold)
                elif message.text == 'Buy':
                    if data[idtg]["tgcoins"] >= 1000:
                        if idtg not in sis["shop"]["standoff"]["gold10"]["id"]:
                            bal = data[idtg]["tgcoins"] - 1000
                            data[idtg]["tgcoins"] = bal
                            sis["shop"]["standoff"]["gold10"]["id"].append(idtg)
                            s = sis["shop"]["standoff"]["gold10"]["quant"] - 1
                            sis["shop"]["standoff"]["gold10"]["quant"] = s
                            absd = "qwertyuiopasdfghjklxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
                            q = ""
                            for i in range(1, 5):
                                a = random.randint(1, 60)
                                q = q + absd[a]
                            with open('bd_telebot.json', 'w') as file:
                                json.dump(data, file, indent=4)
                            with open('sis.json', 'w') as file:
                                    json.dump(sis, file, indent=4)
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                            btn3 = types.KeyboardButton('Back👈🏻')
                            markup.add(btn3)
                            bot.send_message(message.chat.id, f'''
                        Thanks for the purchase🛒

                    Your code: <code>{q}</code>
                    Send him here: https://vk.com/im?media=&sel=-216185000
                            ''',parse_mode='HTML',  reply_markup=markup)
                            bot.send_message(1058097307, f'''
                            {q} - {idtg} 10 голды
                            ''')
                            bot.register_next_step_handler(message, shopgold10back)
                        else:
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                            btn3 = types.KeyboardButton('Back👈🏻')
                            markup.add(btn3)
                            bot.send_message(message.chat.id, f'''
                            You have already bought this product! Wait for the new promotion!
                            ''',  reply_markup=markup)
                            bot.register_next_step_handler(message, shopgold10back)
                    else:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn3 = types.KeyboardButton('Back👈🏻')
                        markup.add(btn3)
                        bot.send_message(message.chat.id, f'''
                        You don't have enough Telecoins! Top up your balance!
                        ''',  reply_markup=markup)
                        bot.register_next_step_handler(message, shopgold10back)
                else:
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Back👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'An error has occurred! Try again!',  reply_markup=markup)
                    bot.register_next_step_handler(message, shopgold10back)
            def shopgold10back(message):
                
                with open('sis.json', 'r') as file:
                    sis = json.load(file)
                with open('bd_telebot.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                reply_markup = types.ReplyKeyboardRemove()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                btn6 = types.KeyboardButton('Buy')
                btn7 = types.KeyboardButton('Back👈🏻')
                markup.add(btn6, btn7)
                bot.send_message(message.chat.id, f'''
10 Gold🍯

Cost: 1000 Telecoins💰

Seller: Telecoin - Coin in Telegram🙍

Quantity: {sis["shop"]["standoff"]["gold10"]["quant"]}
                
1 user - 1 product

❗After the purchase, you will receive a special code that you will need to send to the seller, after which he will tell you how you can get your goods❗

Select the button👇
                ''',  reply_markup=markup)
                bot.register_next_step_handler(message, shopgold10)
            
            def shopback(message):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                btn1 = types.KeyboardButton('Buy Telecoins💳')
                btn2 = types.KeyboardButton('Exchange Telecoins🔄')
                btn3 = types.KeyboardButton('Back👈🏻')
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, f'𝗛𝗲𝗿𝗲 𝘄𝗲 𝗰𝗮𝗻 𝗯𝘂𝘆, 𝗲𝘅𝗰𝗵𝗮𝗻𝗴𝗲 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻𝘀 \n𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻',  reply_markup=markup)
                bot.register_next_step_handler(message, teleshop)
            def shopgameback(message):
                reply_markup = types.ReplyKeyboardRemove()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                btn6 = types.KeyboardButton('Standoff 2🔫')
                btn7 = types.KeyboardButton('Back👈🏻')
                markup.add(btn6, btn7)
                bot.send_message(message.chat.id, f'''
                Choose a game👇
                ''',  reply_markup=markup)
                bot.register_next_step_handler(message, shopgame)
            def shopgoldback(message):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                btn1 = types.KeyboardButton('10 Gold🍯')
                btn3 = types.KeyboardButton('Back👈🏻')
                markup.add(btn1, btn3)
                bot.send_message(message.chat.id, f'''
Here you can exchange Telecoins for gold in Standoff 2🍯

This function is introduced in test mode!💻

Choose a product👇
                ''',  reply_markup=markup)
                bot.register_next_step_handler(message, shopgold)
            def teleshopback(message):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                btn1 = types.KeyboardButton('Buy Telecoins💳')
                btn2 = types.KeyboardButton('Exchange Telecoins🔄')
                btn3 = types.KeyboardButton('Back👈🏻')
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, f'𝗛𝗲𝗿𝗲 𝘄𝗲 𝗰𝗮𝗻 𝗯𝘂𝘆, 𝗲𝘅𝗰𝗵𝗮𝗻𝗴𝗲 𝗧𝗲𝗹𝗲𝗰𝗼𝗶𝗻𝘀\n𝗖𝗹𝗶𝗰𝗸 𝗼𝗻 𝘁𝗵𝗲 𝗯𝘂𝘁𝘁𝗼𝗻👇🏻',  reply_markup=markup)
                bot.register_next_step_handler(message, teleshop)
            @bot.message_handler(content_types=["text"])
            def osh(message):
                bot.send_message(message.chat.id, f"I didn't understand what you wrote) Write: /start")
            bot.polling(none_stop=True)
        except:
            w = 1
main()