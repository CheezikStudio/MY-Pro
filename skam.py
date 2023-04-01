# 5864026204:AAEtczPU-Qfd1P4Naiuo-zdVCa-PIiaaYRM
import telebot 
import time
import json
from telebot import types
import random
def main():
    while True:
        try:
            bot = telebot.TeleBot('5864026204:AAEtczPU-Qfd1P4Naiuo-zdVCa-PIiaaYRM')
            @bot.message_handler(commands=["start"])
            def start(message, res=False):
                print(1111111111)
                with open('skam_bd.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                with open('skam_stats.json', 'r') as file:
                    stats = json.load(file)
                idtg = str(message.from_user.id)
                w = 0
                if idtg not in data:
                    if " " in message.text:
                        try:
                            data[message.text.split()[1]]["ref"] += 1
                            data[message.text.split()[1]]["gold"] += 1
                            bot.send_message(message.text.split()[1], text=f'''Вам начисленно - 1G за реферала!''')
                            with open('skam_bd.json', 'w') as file:
                                json.dump(data, file, indent=4)
                            w = 1
                        except:
                            pass
                    with open('skam_bd.json', 'r') as file:
                        data = json.load(file)
                    name = str(message.chat.first_name)
                    idtg = str(message.from_user.id)
                    people = {"fio": message.from_user.first_name, "gold": 0, "id":  message.from_user.username, "v": [], "ref": 0, "dop": {}}
                    data[idtg] = people
                    with open('skam_bd.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    global t
                    t = time.time()
                    if w == 1:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                        btn1 = types.KeyboardButton('Заработать G💰')
                        btn2 = types.KeyboardButton('Реф. программа👥')
                        btn3 = types.KeyboardButton('Раздача🎁')
                        btn4 = types.KeyboardButton('Профиль🙍‍♂')
                        markup.add(btn1, btn2, btn3, btn4)
                        if idtg == "1058097307":
                            btn11 = types.KeyboardButton('Админ Меню')
                            markup.add(btn11)
                        bot.send_message(message.chat.id, f'''
            <i><b>Информация📜</b></i>

    <b><i>Статистика бота:</i></b>
    <b>Пользуются GiveGold: {len(data)}👥</b>
    <b>Заработано G: {stats["stats"]["gold"]}💰</b>

    ------------------------------

    <b><i>Ваша мини-статистика:</i></b>

    <b>Имя: {data[idtg]["fio"]}🙍‍♂</b>
    <b>Баланс: {data[idtg]["gold"]}💰</b>

    <i>Выберите кнопку👇🏻</i>
                        ''',  reply_markup=markup, parse_mode='HTML')
                if message.text == "/start" or message.text == "/menu":
                    t1 = time.time()
                    if t1 - t >= 2:
                        print(1111)
                    else:
                        
                        t = time.time()
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                        btn1 = types.KeyboardButton('Заработать G💰')
                        btn2 = types.KeyboardButton('Реф. программа👥')
                        btn3 = types.KeyboardButton('Раздача🎁')
                        btn4 = types.KeyboardButton('Профиль🙍‍♂')
                        markup.add(btn1, btn2, btn3, btn4)
                        if idtg == "1058097307":
                            btn11 = types.KeyboardButton('Админ Меню')
                            markup.add(btn11)
                        bot.send_message(message.chat.id, f'''
            <i><b>Информация📜</b></i>

    <b><i>Статистика бота:</i></b>
    <b>Пользуются GiveGold: {len(data)}👥</b>
    <b>Заработано G: {stats["stats"]["gold"]}💰</b>

    ------------------------------

    <b><i>Ваша мини-статистика:</i></b>

    <b>Имя: {data[idtg]["fio"]}🙍‍♂</b>
    <b>Баланс: {data[idtg]["gold"]}💰</b>
    <b>Выполнено заданий: {len(data[idtg]["v"])}💰</b>

    <i>Выберите кнопку👇🏻</i>
                        ''',  reply_markup=markup, parse_mode='HTML')
                    
            @bot.message_handler(content_types=["text"])
            def menu(message, res=False):
                with open('skam_bd.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                with open('skam_stats.json', 'r') as file:
                    stats = json.load(file)
                if message.text == "Админ Меню" and idtg == "1058097307":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Добавить задание➕')
                    btn2 = types.KeyboardButton('Рассылка💬')
                    btn3 = types.KeyboardButton("База данных🗒")
                    btn4 = types.KeyboardButton('В меню📜')
                    markup.add(btn1, btn2, btn3, btn4)
                    bot.send_message(message.chat.id, f'''
        <i><b>Информация📜</b></i>

<b><i>Статистика бота:</i></b>
<b>Пользуются GiveGold: {len(data)}👥</b>
<b>Заработано G: {stats["stats"]["gold"]}💰</b>
<b>Выполнено заданий: {stats["stats"]["vip"]}</b>

<i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, admin)
                elif message.text == "Заработать G💰":
                    w = 0
                    for i in stats["zad"]:
                        if i not in data[idtg]["v"]: 
                            try:
                                markup = types.InlineKeyboardMarkup(row_width = 1)
                                btn1 = types.InlineKeyboardButton(text="Ссылка", url= stats["zad"][i]["url"])
                                btn2 = types.InlineKeyboardButton(text="Я выполнил✅", callback_data=f"zad {i}")
                                markup.add(btn1, btn2)
                                bot.send_message(message.chat.id, f'''
                            <b>Найдено задание!</b>
                            
                    {stats["zad"][i]["text"]}
                            
                    Оплата: {stats["zad"][i]["gold"]}''',  reply_markup=markup, parse_mode='HTML')
                                w = 1 
                                break
                            except:
                                markup = types.InlineKeyboardMarkup(row_width = 1)
                                btn2 = types.InlineKeyboardButton(text="Я выполнил✅", callback_data=f"zad {i}")
                                markup.add(btn2)
                                bot.send_message(message.chat.id, f'''
                            <b>Найдено задание!</b>
                            
                    {stats["zad"][i]["text"]}
                            
                    Оплата: {stats["zad"][i]["gold"]}''',  reply_markup=markup, parse_mode='HTML')
                                w = 1 
                                break
                    if w == 0:   
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                        btn1 = types.KeyboardButton('В меню📜')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f"Для вас нет доступных заданий!",  reply_markup=markup)
                elif message.text == "В меню📜":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Заработать G💰')
                    btn2 = types.KeyboardButton('Реф. программа👥')
                    btn3 = types.KeyboardButton('Раздача🎁')
                    btn4 = types.KeyboardButton('Профиль🙍‍♂')
                    markup.add(btn1, btn2, btn3, btn4)
                    if idtg == "1058097307":
                        btn11 = types.KeyboardButton('Админ Меню')
                        markup.add(btn11)
                    bot.send_message(message.chat.id, f'''
        <i><b>Информация📜</b></i>

<b><i>Статистика бота:</i></b>
<b>Пользуются GiveGold: {len(data)}👥</b>
<b>Заработано G: {stats["stats"]["gold"]}💰</b>

------------------------------

<b><i>Ваша мини-статистика:</i></b>

<b>Имя: {data[idtg]["fio"]}🙍‍♂</b>
<b>Баланс: {data[idtg]["gold"]}💰</b>
<b>Выполнено заданий: {len(data[idtg]["v"])}💰</b>

<i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                elif message.text == "Реф. программа👥":
                    bot.send_message(message.chat.id, f'''
        <i><b>Реф. программа👥</b></i>
<b>Приглашай друзей и получай 1G!</b>

<b>Ты пригласил: {data[idtg]["ref"]}</b>
Твоя ссылка: <code>{"https://t.me/GiveSOGold_bot?start="+idtg}</code>

<i>Отсылай друзьям эту ссылку друьям и получай своё золото после как они перейдут по ней!
*Нажми на ссылку чтобы скопировать</i>
                    ''',  parse_mode='HTML')
                elif message.text == "Раздача🎁":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Участвовать🎁')
                    btn2 = types.KeyboardButton('В меню📜')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
            <i><b>Раздача🎁</b></i>
    <b>Ежедневная раздача!</b>

🎁ПРИЗ: 250 GOLD🎁

Участников: {len(stats["roz"]["pip"])}
Для участия нужно только нажать кнопку 'Участвовать🎁'!

Итоги каждый день в 15:00 по МСК!
                    ''',  reply_markup=markup, parse_mode='HTML')
                elif message.text == "Участвовать🎁":
                    if idtg in stats["roz"]["pip"]: 
                        bot.send_message(message.chat.id, f"Вы уже участвуете!")
                    else:
                        stats["roz"]["pip"].append(idtg)
                        with open('skam_stats.json', 'w') as file:
                            json.dump(stats, file, indent=4)
                        bot.send_message(message.chat.id, f"Молодец! Жди итогов, если ты выиграешь, то тебе на баланс придёт приз!")
                elif message.text == "Профиль🙍‍♂":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Вывести G💰')
                    btn2 = types.KeyboardButton('В меню📜')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
            <i><b>Профиль🙍‍♂</b></i>
    <b>Имя: {data[idtg]["fio"]}🙍‍♂</b>
    <b>Баланс: {data[idtg]["gold"]}G💰</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                elif message.text == "Вывести G💰":
                    if data[idtg]["gold"] >= 100:
                        bot.send_message(message.chat.id, f"Молодец! Пиши сюда: @devinpython что хочешь вывести!\nID: {idtg}")
                    else:
                        bot.send_message(message.chat.id, f"Минимальный вывод - 100G💰")
                else:
                    bot.send_message(message.chat.id, f"Я тебя не понял! Нажми: /start")
            def admin(message):
                with open('skam_bd.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                with open('skam_stats.json', 'r') as file:
                    stats = json.load(file)
                if message.text == "В меню📜":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Заработать G💰')
                    btn2 = types.KeyboardButton('Реф. программа👥')
                    btn3 = types.KeyboardButton('Раздача🎁')
                    btn4 = types.KeyboardButton('Профиль🙍‍♂')
                    markup.add(btn1, btn2, btn3, btn4)
                    if idtg == "1058097307":
                        btn11 = types.KeyboardButton('Админ Меню')
                        markup.add(btn11)
                    bot.send_message(message.chat.id, f'''
        <i><b>Информация📜</b></i>

<b><i>Статистика бота:</i></b>
<b>Пользуются GiveGold: {len(data)}👥</b>
<b>Заработано G: {stats["stats"]["gold"]}💰</b>

------------------------------

<b><i>Ваша мини-статистика:</i></b>

<b>Имя: {data[idtg]["fio"]}🙍‍♂</b>
<b>Баланс: {data[idtg]["gold"]}💰</b>
<b>Выполнено заданий: {len(data[idtg]["v"])}💰</b>

<i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                elif message.text == "Рассылка💬":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn3 = types.KeyboardButton('Отмена!')
                    markup.add(btn3)
                    bot.send_message(message.from_user.id, "Текст:",  reply_markup=markup)
                    bot.register_next_step_handler(message, rassilka)
                elif message.text == "Добавить задание➕":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn3 = types.KeyboardButton('Отмена!')
                    markup.add(btn3)
                    bot.send_message(message.from_user.id, "Текст задания:",  reply_markup=markup)
                    bot.register_next_step_handler(message, dop_url)
            def rassilka(message):
                with open('skam_bd.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                with open('skam_stats.json', 'r') as file:
                    stats = json.load(file)
                if message.text == "Отмена!":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Добавить задание➕')
                    btn2 = types.KeyboardButton('Рассылка💬')
                    btn3 = types.KeyboardButton("База данных🗒")
                    btn4 = types.KeyboardButton('В меню📜')
                    markup.add(btn1, btn2, btn3, btn4)
                    bot.send_message(message.chat.id, f'''
        <i><b>Информация📜</b></i>

<b><i>Статистика бота:</i></b>
<b>Пользуются GiveGold: {len(data)}👥</b>
<b>Заработано G: {stats["stats"]["gold"]}💰</b>
<b>Выполнено заданий: {stats["stats"]["vip"]}</b>

<i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, admin)
                else:
                    gsd = 0
                    for k in data:
                        try:
                            bot.send_message(k, message.text, parse_mode='HTML')
                            gsd += 1
                        except :
                            pass
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn3 = types.KeyboardButton('Админ Меню')
                    markup.add(btn3)
                    bot.send_message(message.from_user.id, f"Готово! Отправленно: {gsd} сообщений!",  reply_markup=markup)
            def dop_url(message):
                with open('skam_bd.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                with open('skam_stats.json', 'r') as file:
                    stats = json.load(file)
                if message.text == "Отмена!":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Добавить задание➕')
                    btn2 = types.KeyboardButton('Рассылка💬')
                    btn3 = types.KeyboardButton("База данных🗒")
                    btn4 = types.KeyboardButton('В меню📜')
                    markup.add(btn1, btn2, btn3, btn4)
                    bot.send_message(message.chat.id, f'''
        <i><b>Информация📜</b></i>

<b><i>Статистика бота:</i></b>
<b>Пользуются GiveGold: {len(data)}👥</b>
<b>Заработано G: {stats["stats"]["gold"]}💰</b>
<b>Выполнено заданий: {stats["stats"]["vip"]}</b>

<i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, admin)
                else:
                    text = message.text
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn3 = types.KeyboardButton("Задание без ссылки")
                    btn4 = types.KeyboardButton("Отмена!")
                    markup.add(btn3, btn4)
                    bot.send_message(message.from_user.id, f"Ссылка:",  reply_markup=markup)
                    bot.register_next_step_handler(message, dop_sum, text)
            def dop_sum(message, text):
                with open('skam_bd.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                with open('skam_stats.json', 'r') as file:
                    stats = json.load(file)
                if message.text == "Отмена!":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Добавить задание➕')
                    btn2 = types.KeyboardButton('Рассылка💬')
                    btn3 = types.KeyboardButton("База данных🗒")
                    btn4 = types.KeyboardButton('В меню📜')
                    markup.add(btn1, btn2, btn3, btn4)
                    bot.send_message(message.chat.id, f'''
        <i><b>Информация📜</b></i>

<b><i>Статистика бота:</i></b>
<b>Пользуются GiveGold: {len(data)}👥</b>
<b>Заработано G: {stats["stats"]["gold"]}💰</b>
<b>Выполнено заданий: {stats["stats"]["vip"]}</b>

<i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, admin)
                else:
                    url = message.text
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn3 = types.KeyboardButton("Отмена!")
                    markup.add(btn3)
                    bot.send_message(message.from_user.id, f"Стоимость:",  reply_markup=markup)
                    bot.register_next_step_handler(message, dop, text, url)
            def dop(message, text, url):
                with open('skam_bd.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                with open('skam_stats.json', 'r') as file:
                    stats = json.load(file)
                if message.text == "Отмена!":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Добавить задание➕')
                    btn2 = types.KeyboardButton('Рассылка💬')
                    btn3 = types.KeyboardButton("База данных🗒")
                    btn4 = types.KeyboardButton('В меню📜')
                    markup.add(btn1, btn2, btn3, btn4)
                    bot.send_message(message.chat.id, f'''
        <i><b>Информация📜</b></i>

<b><i>Статистика бота:</i></b>
<b>Пользуются GiveGold: {len(data)}👥</b>
<b>Заработано G: {stats["stats"]["gold"]}💰</b>
<b>Выполнено заданий: {stats["stats"]["vip"]}</b>

<i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, admin)
                else:
                    sum = message.text
                    stats["zad"][str(random.randint(1, 100000))] = {"text": text, "url": url, "gold": sum}
                    with open('skam_stats.json', 'w') as file:
                        json.dump(stats, file, indent=4)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn3 = types.KeyboardButton('Админ Меню')
                    markup.add(btn3)
                    bot.send_message(message.from_user.id, f"Готово!",  reply_markup=markup)
            @bot.callback_query_handler(func=lambda call: True)
            def call_menu(call):
                with open('skam_bd.json', 'r') as file:
                    data = json.load(file)
                idtg = str(call.from_user.id)
                with open('skam_stats.json', 'r') as file:
                    stats = json.load(file)
                if call.data.split(" ")[0] == "zad":
                    data[idtg]["v"].append(call.data.split(" ")[1])
                    with open('skam_bd.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn3 = types.KeyboardButton('В меню📜')
                    markup1.add(btn3)
                    bot.send_message(chat_id=call.from_user.id, text=f"Спасибо за выполнение! Ожидайте проверки!",  reply_markup=markup1)
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardButton(text="Выполнил✅", callback_data=f'''vip {idtg} {stats["zad"][call.data.split(" ")[1]]["gold"]}''')
                    btn2 = types.InlineKeyboardButton(text="Нет", callback_data=f"novip {idtg}")
                    markup.add(btn1, btn2)
                    bot.send_message(1058097307, f'''
                    Заявка!
                    {idtg} - {call.data.split(" ")[1]}
                    ''',  reply_markup=markup)
                elif call.data.split(" ")[0] == "vip":
                    bot.send_message(call.data.split(" ")[1], text=f'''Спасибо за выполнение задания! Вам начисленно - {call.data.split(" ")[2]}G''')
                    data[idtg]["gold"] += int(call.data.split(" ")[2])
                    stats["stats"]["gold"] += int(call.data.split(" ")[2])
                    stats["stats"]["vip"] += 1
                    with open('skam_bd.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    with open('skam_stats.json', 'w') as file:
                        json.dump(stats, file, indent=4)
                elif call.data.split(" ")[0] == "novip":
                    bot.send_message(call.data.split(" ")[1], text=f'''Задание прошло проверку! К сожалению оно выполнено не правильно!''')
            bot.polling(none_stop=False)
        except:
            pass
main()