# -*- coding: utf8 -*-
import telebot 
import time
import json
import random
import heapq
from telebot import types
from pyKeksik import KeksikApi
from types import *
def main():
    
    
    while True:
        w = 1
        try:
            bot = telebot.TeleBot('5631029047:AAHUc2qMrbGiovxgRdpG1AEh72PX4pOb2Jo')
            @bot.message_handler(commands=["start"])
            def start(message, res=False):
                with open('zeus.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if idtg not in data:
                    with open('zeus.json', 'r') as file:
                        data = json.load(file)
                    name = str(message.chat.first_name)
                    idtg = str(message.from_user.id)
                    rbr = {"name": name, "gold" : 0, "gold_kup" : 0, "email": "❌", "dop1": [], "dop2": {}, "dop3": ""}
                    data[idtg] = rbr
                    with open('zeus.json', 'w') as file:
                        json.dump(data, file, indent=4)
                else:
                    with open('zeus.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Золото💰')
                    btn2 = types.KeyboardButton('Игры🎮')
                    btn3 = types.KeyboardButton('Розыгрыш🎁')
                    btn4 = types.KeyboardButton('Отзывы📜')
                    btn5 = types.KeyboardButton('Профиль🙍‍♂')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    k = 0
                    for i in data:
                        k += data[idtg]["gold_kup"]
                    file = open("glmenu.jpg", "rb")
                    bot.send_photo(message.chat.id, file, f'''
            <i><b>ГЛАВНОЕ МЕНЮ</b></i>

    <b>------ТВОЯ СТАТИСТИКА------</b>

Имя: {data[idtg]["name"]}🙍‍♂
Баланс: {data[idtg]["gold"]} золота💰
Куплено золота: {data[idtg]["gold_kup"]}🛒

    <b>------СТАТИСТИКА ПРОЕКТА------</b>

Всего людей: {len(data)}🙍‍♂
Всего куплено: {k}🛒
 

    <i>Нажимай на кнопку, не стесняйся👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    
                    bot.register_next_step_handler(message, zeus)
            def zeus(message):
                with open('zeus.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                
                if message.text == 'Золото💰':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Купить золото🛒')
                    btn2 = types.KeyboardButton('Вывести золото🛫')
                    btn3 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                    <i><b>ЗОЛОТО</b></i>

Баланс: {data[idtg]["gold"]}💰

<i>Нажимай на кнопку, не стесняйся👇🏻</i>
                    
                    
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, zoloto)
                elif message.text == 'Игры🎮':
                    pass
                elif message.text == 'Розыгрыш🎁':
                    with open('zeus.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    top1 = []
                    top2 = {}
                    for i in data:
                        try:
                            b = data[i]["gold_kup"]
                            n = data[i]["name"]
                            a = (b, n)
                            top1.append(a)
                        except:
                            r = 1
                    top2 = heapq.nlargest(3, top1)
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    
                    bot.send_message(message.chat.id, f'''
                    <i><b>РОЗЫГРЫШ</b></i>

Топ лучших покупателей👇🏻
🥇 {top2[0][1]} | {top2[0][0]} золота🛒
🥈 {top2[1][1]} | {top2[1][0]} золота🛒
🥉 {top2[2][1]} | {top2[2][0]} золота🛒

Среди них будет разыграно: <b>BATTLE PASS</b> И <b>ЗОЛОТО</b>!

Призы:
🥇 - <b>BATTLE PASS "Project Pandora"</b>👻
🥈 - 200 Золота💰
🥉 - 100 Золота💰

Чтобы занять одно из этих мест, сделай покупку в нашем боте на сумму больше всех🏅

Ты купил: {data[i]["gold_kup"]} золота🛒

<i>*Итоги будут за 5 дней до окончания батл пасса</i>

<i>Нажимай на кнопку, не стесняйся👇🏻</i>


                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, start)
                elif message.text == 'Отзывы📜':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Отзывы ты можешь постреть: <a href = "https://t.me/ZeusGoldOtzivy">тут</a>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, start)
                elif message.text == 'Профиль🙍‍♂':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Промокод💎')
                    btn2 = types.KeyboardButton('Реферальная программа💸')
                    btn3 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                    <i><b>ПРОФИЛЬ</b></i>
        

                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, start)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Я тебя не понял(( Возвращайся обратно!
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, start)
            def zoloto(message):
                with open('zeus.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Золото💰')
                    btn2 = types.KeyboardButton('Игры🎮')
                    btn3 = types.KeyboardButton('Розыгрыш🎁')
                    btn4 = types.KeyboardButton('Отзывы📜')
                    btn5 = types.KeyboardButton('Профиль🙍‍♂')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    k = 0
                    for i in data:
                        k += data[idtg]["gold_kup"]
                    file = open("glmenu.jpg", "rb")
                    bot.send_photo(message.chat.id, file, f'''
            <i><b>ГЛАВНОЕ МЕНЮ</b></i>

    <b>------ТВОЯ СТАТИСТИКА------</b>

Имя: {data[idtg]["name"]}🙍‍♂
Баланс: {data[idtg]["gold"]} золота💰
Куплено золота: {data[idtg]["gold_kup"]}🛒

    <b>------СТАТИСТИКА ПРОЕКТА------</b>

Всего людей: {len(data)}🙍‍♂
Всего куплено: {k}🛒
 

    <i>Нажимай на кнопку, не стесняйся👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    
                    bot.register_next_step_handler(message, zeus)
                elif message.text == 'Купить золото🛒':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Купить🛒')
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
                    <i><b>ЗОЛОТО</b></i>
📊<b>Курс - {data["1058097307"]["dop2"]["kurs"]} = 1 Золоту</b>📊

Баланс: {data[idtg]["gold"]}💰

<i>Нажимай на кнопку, если хочешь купить👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, zoloto_buy)
                elif message.text == 'Вывести золото🛫':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn2)
                    bot.send_message(message.chat.id, f'Перед покупкой обязательно ознакомься с правилами:https://telegra.ph/Pravila-polzovaniya-botom-11-07\nНапиши сумму вывода (min - 100 Золота):',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, zoloto_viv)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Я тебя не понял(( Возвращайся обратно!
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, start)
            def zoloto_buy(message):
                with open('zeus.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Купить золото🛒')
                    btn2 = types.KeyboardButton('Вывести золото🛫')
                    btn3 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                    <i><b>ЗОЛОТО</b></i>

Баланс: {data[idtg]["gold"]}💰

<i>Нажимай на кнопку, не стесняйся👇🏻</i>
                    
                    
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, zoloto)
                elif message.text == 'Купить🛒':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Проверить оплату🔄')
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
                    <i><b>ЗОЛОТО</b></i>
📊<b>Курс - {data["1058097307"]["dop2"]["kurs"]}рублей = 1 Золото</b>📊
        
Чтобы купить нужно:
1 - Перейти по ссылке: https://vk.com/the.telecoin?w=app6887721_-216185000
2 - Нажимаем на кнопку "Хочу помочь в развитии!"
3 - Вводим сумму и добавляем в комментарий свой ID
ID - <code>{idtg}</code>
4 - Нажимаем "Отправить донат"
5 - После выбираем способ оплаты и донатим
6 - После нажимаем "Проверить оплату🔄"
7 - !Бот сам расчитает колличество золота!
8 - Готово!
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, zoloto_buy_pro)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Я тебя не понял(( Возвращайся обратно!
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, start)
            def zoloto_buy_pro(message):
                with open('zeus.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Купить🛒')
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
                    <i><b>ЗОЛОТО</b></i>
📊<b>Курс - {data["1058097307"]["dop2"]["kurs"]} = 1 Золото</b>📊

Баланс: {data[idtg]["gold"]}💰

<i>Нажимай на кнопку, если хочешь купить👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, zoloto_buy)
                else:
                    apikey = "bff7ed3ca6510d2af385f7963f81eedd2accd04a27a0cd6a4d"
                    group_id = 216185000
                    keksik_api = KeksikApi(group_id, apikey)
                    with open('zeus.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    t = keksik_api.donates.get()
                    print(t)
                    tlen = len(t)
                    print(tlen)
                    for i in (0, tlen - 1):
                        if t[i].msg == idtg:
                            if t[i].date not in data[idtg]["dop1"]:
                                sum = round(int(t[i].amount) / data["1058097307"]["dop2"]["kurs"])

                                pol1 = data[idtg]["gold"] + int(sum)
                                pol2 = data[idtg]["gold_kup"] + int(sum)
                                data[idtg]["dop1"].append(t[i].date)
                                data[idtg]["gold"] = pol1
                                data[idtg]["gold_kup"] = pol2
                                with open('zeus.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                                btn3 = types.KeyboardButton('Back👈🏻')
                                markup.add(btn3)
                                bot.send_message(message.chat.id, f'Был совершён перевод на сумму - {sum} золота✅',  reply_markup=markup)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Проверить оплату🔄')
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
                    <i><b>ЗОЛОТО</b></i>
📊<b>Курс - {data["1058097307"]["dop2"]["kurs"]}рублей = 1 Золото</b>📊
        
Чтобы купить нужно:
1 - Перейти по ссылке: https://vk.com/the.telecoin?w=app6887721_-216185000
2 - Нажимаем на кнопку "Хочу помочь в развитии!"
3 - Вводим сумму и добавляем в комментарий свой ID
ID - <code>{idtg}</code>
4 - Нажимаем "Отправить донат"
5 - После выбираем способ оплаты и донатим
6 - После нажимаем "Проверить оплату🔄"
7 - !Бот сам расчитает колличество золота!
8 - Готово!
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, zoloto_buy_pro)
            def zoloto_viv(message):
                with open('zeus.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Купить золото🛒')
                    btn2 = types.KeyboardButton('Вывести золото🛫')
                    btn3 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                    <i><b>ЗОЛОТО</b></i>

Баланс: {data[idtg]["gold"]}💰

<i>Нажимай на кнопку, не стесняйся👇🏻</i>
                    
                    
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, zoloto)
                else:
                    try:
                        if int(message.text) >= 100:
                            if data[idtg]["gold"] >= int(message.text):
                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                                btn1 = types.KeyboardButton('Назад👈🏻')
                                markup.add(btn1)
                                bot.send_message(message.chat.id, f'''
Молодец!

Остался последний шаг!

Отошли мне скриншот выставленого скина у которого менее 15.000 запросов на продажу за <b><code>{round(int(message.text) + int(message.text) * 0.25)}.34</code></b>!

Нажми чтобы скопировать: <code>{round(int(message.text) + int(message.text) * 0.25)}.34</code>

<b>Золото спишится после отправления скриншота)</b>
                                ''',  reply_markup=markup, parse_mode='HTML')
                                bot.register_next_step_handler(message, skr, message)
                    except:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                    Я тебя не понял(( Возвращайся обратно!
                        ''',  reply_markup=markup, parse_mode='HTML')







            def skr(message, m):
                with open('zeus.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Купить🛒')
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
                    <i><b>ЗОЛОТО</b></i>
📊<b>Курс - {data["1058097307"]["dop2"]["kurs"]} = 1 Золото</b>📊

Баланс: {data[idtg]["gold"]}💰

<i>Нажимай на кнопку, если хочешь купить👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, zoloto_buy)
                if message.content_type == 'document':
                    pol1 = data[idtg]["gold"] - int(m)
                    data[idtg]["gold"] = pol1
                    
                    with open('zeus.json', 'w') as file:
                        json.dump(data, file, indent=4)











            
            bot.polling(none_stop=True)
        except:
            pass
main()