# 5695928648:AAFhb5HB8clzMQ2wFSb3dEvpdufIfH3Yg2Q - Учитель
import telebot 
import json
from telebot import types
import random
import config
def main():
    while True:
        if True:
            bot = telebot.TeleBot('5695928648:AAFhb5HB8clzMQ2wFSb3dEvpdufIfH3Yg2Q')
            @bot.message_handler(commands=["start"])
            def start(message, res=False):
                idtg = str(message.from_user.id)
                with open('uchitel.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == "/start" or message.text == "/menu":
                    if idtg not in data:
                        bot.send_message(message.chat.id, f'''
<i><b>Регистрация</b></i>
<b>Введите пожалуйста код учителя:</b>
                    ''', parse_mode='HTML')
                        bot.register_next_step_handler(message, regis)
                    else:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton(text="Квантумы👩‍🏫")
                        markup.add(btn1)
                        bot.send_message(message.chat.id, config.menu_uchitel(idtg), parse_mode='HTML', reply_markup=markup)
            def regis(message):
                with open('logins.json', 'r') as file:
                    logins = json.load(file)
                idtg = str(message.from_user.id)
                e = 2
                if message.text in logins["uchitel"]:
                    e = 1  
                    
                if e != 1:
                    bot.send_message(message.chat.id, f'''
<i><b>ОШИБКА!</b></i>
<b>Введите пожалуйста код учителя:</b>
                    ''', parse_mode='HTML')
                    bot.register_next_step_handler(message, regis)

                if e == 1:
                    with open('uchitel.json', 'r') as file:
                        data = json.load(file)
                    name = str(message.chat.first_name)
                    idtg = str(message.from_user.id)
                    rbr = {"fio": logins["uchitel"][str(message.text)]["fio"], "kvan": [], "dop" : {"name": message.from_user.username}}
                    data[idtg] = rbr
                    with open('uchitel.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    with open('uchitel.json', 'r') as file:
                        data = json.load(file)
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardButton(text="В меню📅", callback_data="menu")
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
    <b>Спасибо за регистрацию!</b>
<i>{data[idtg]["fio"]} нажмите на кнопку "В меню📅" чтобы прейти в главное меню!</i>
                    ''',  reply_markup=markup, parse_mode='HTML')



            @bot.message_handler(content_types=["text"])
            def menu(message, res=False):
                with open('uchitel.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                with open('kvantorium.json', 'r') as file:
                    kvant = json.load(file)
                if message.text == "Создать квантум":
                    markup = types.ReplyKeyboardMarkup(row_width = 1)
                    btn1 = types.KeyboardButton(text="Назад👈🏻")
                    markup.add(btn1)
                    bot.send_message(message.chat.id, config.dopkvant, parse_mode='HTML', reply_markup=markup)
                    bot.register_next_step_handler(message, dop)
                if message.text == "В меню📅":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton(text="Квантумы👩‍🏫")
                    markup.add(btn1)
                    bot.send_message(message.chat.id, config.menu_uchitel(idtg), parse_mode='HTML', reply_markup=markup)
                if message.text == "Квантумы👩‍🏫" or message.text == "К квантумам👩‍🏫":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    for i in data[idtg]["kvan"]:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    btn4 = types.KeyboardButton('Создать квантум')
                    markup.add(btn4)
                    btn5 = types.KeyboardButton('В меню📅')
                    markup.add(btn5)
                    bot.send_message(message.chat.id, config.uchitel_kvant, parse_mode='HTML', reply_markup=markup)
                if message.text in data[idtg]["kvan"] or message.text == "Вернуться👈🏻":
                    if message.text in data[idtg]["kvan"]:
                        global naz
                        naz = message.text
                    reply_markup=types.ReplyKeyboardRemove()
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardButton(text='Расписание📅',  callback_data="ras")
                    btn2 = types.InlineKeyboardButton(text='Ученики🙍‍♂️',  callback_data="uch")
                    btn3 = types.InlineKeyboardButton(text='Описание квантума💬',  callback_data="opis")
                    btn4 = types.InlineKeyboardButton(text='Рассылка📤',  callback_data="rassilka")
                    btn5 = types.InlineKeyboardButton(text='Назад👈🏻',  callback_data="kvant")
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(message.chat.id, config.kvant(naz, idtg),  reply_markup=markup, parse_mode='HTML')
                if message.text == "Добавить день➕":
                    d = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    for i in d:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    btn2 = types.KeyboardButton('Отмена!')
                    markup.add(btn2)
                    bot.send_message(message.chat.id, config.dop_day,  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, day)


                    
            def day(message):
                with open('uchitel.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                with open('kvantorium.json', 'r') as file:
                    kvant = json.load(file)
                if message.text == 'Отмена!':
                    reply_markup=types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    try:
                        for i in kvant[naz]["ras"]:
                            try:
                                btn1 = types.KeyboardButton(i)
                                markup.add(btn1)
                            except:
                                pass
                    except:
                        pass
                    btn4 = types.KeyboardButton('Добавить день➕')
                    markup.add(btn4)
                    btn5 = types.KeyboardButton('Вернуться👈🏻')
                    markup.add(btn5)
                    bot.send_message(idtg, config.ras,  parse_mode='HTML', reply_markup=markup)
                elif message.text in ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]:
                    with open('kvantorium.json', 'r') as file:
                        kvant = json.load(file)
                    kvant[naz]["ras"][message.text] = {"ras_str" : "", "ras_bd": []}
                    with open('kvant.json', 'w') as file:
                        json.dump(kvant, file, indent=4)
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardButton(text="Назад👈🏻", callback_data="ras")
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
<i>День успешно добавлен!</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                else:
                    d = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    for i in d:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    btn2 = types.KeyboardButton('Отмена!')
                    markup.add(btn2)
                    bot.send_message(message.chat.id, config.dop_day,  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, day)


            def dop(message):
                with open('uchitel.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                with open('kvantorium.json', 'r') as file:
                    kvant = json.load(file)
                if message.text == "Назад👈🏻" or message.text == "Создать квантум":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    for i in data[idtg]["kvan"]:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    btn4 = types.KeyboardButton('Создать квантум')
                    markup.add(btn4)
                    btn5 = types.KeyboardButton('В меню📅')
                    markup.add(btn5)
                    bot.send_message(message.chat.id, config.uchitel_kvant, parse_mode='HTML', reply_markup=markup)
                else:
                    with open('uchitel.json', 'r') as file:
                        data = json.load(file)
                    with open('kvantorium.json', 'r') as file:
                        kvant = json.load(file)
                    rbr = {"ras" : {}, "ludi" : {}, "dop" : {"bio": {"text": "Не заполнено!", "kv": "❌", "opis": "❌"}}}
                    kvant[message.text] = rbr
                    data[idtg]["kvan"].append(message.text)
                    with open('kvantorium.json', 'w') as file:
                        json.dump(kvant, file, indent=4)
                    with open('uchitel.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('К квантумам👩‍🏫')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    <i>Квантум успешно создан</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    
            @bot.callback_query_handler(func=lambda call: True)
            def call_menu(call):
                with open('uchitel.json', 'r') as file:
                    data = json.load(file)
                idtg = str(call.from_user.id)
                with open('kvantorium.json', 'r') as file:
                    kvant = json.load(file)
                if call.data == "menu":
                    reply_markup=types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton(text="Квантумы👩‍🏫")
                    markup.add(btn1)
                    bot.send_message(call.from_user.id, config.menu_uchitel(idtg), parse_mode='HTML', reply_markup=markup)
                if call.data == "ras":
                    reply_markup=types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    try:
                        for i in kvant[naz]["ras"]:
                            try:
                                btn1 = types.KeyboardButton(i)
                                markup.add(btn1)
                            except:
                                pass
                    except:
                        pass
                    btn4 = types.KeyboardButton('Добавить день➕')
                    markup.add(btn4)
                    btn5 = types.KeyboardButton('К квантумам👩‍🏫')
                    markup.add(btn5)
                    bot.send_message(call.from_user.id, config.ras,  parse_mode='HTML', reply_markup=markup)

            bot.polling(none_stop=True, timeout=20000)
        else:
            pass
main()