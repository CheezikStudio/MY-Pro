# 5695928648:AAFhb5HB8clzMQ2wFSb3dEvpdufIfH3Yg2Q - Учитель
import telebot 
import json
from telebot import types
import random
def main():
    while True:
        if True:
            bot = telebot.TeleBot('5695928648:AAFhb5HB8clzMQ2wFSb3dEvpdufIfH3Yg2Q')
            @bot.message_handler(commands=["start"])
            def start(message, res=False):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if idtg not in data:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Ученик🙍‍♂')
                    btn2 = types.KeyboardButton('Учитель👩‍🏫')
                    markup.add(btn1, btn2)
                    file = open("image.png", "rb")
                    bot.send_photo(message.chat.id, file, f'''
            <i><b>Регистрация</b></i>
<b>Ваши данные отсутствуют в базе данных! Для этого просим пройти регистрацию!</b>

<b>Кто вы?</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    print(message)
                    bot.register_next_step_handler(message, regis1)

                elif data[idtg]["dop"]["user"] == "1":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Квантумы👩‍🏫')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                <i><b>Информация📜</b></i>

        <b>ФИО: {data[idtg]["fio"]}</b>🙍‍♂
        
        <i>Нажмите на кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    print(message.text)
                    bot.register_next_step_handler(message, menu_uch)
                elif data[idtg]["dop"]["user"] == "0":
                    e = 2
                    kv = []
                    id = {}
                    for i in data:
                        try:
                            for k in data[i]["kvan"]:
                                try:
                                    for l in data[i]["kvan"][k]["ludi"]:
                                        if data[idtg]["fio"] == l:
                                            data[i]["kvan"][k]["ludi"][data[idtg]["fio"]] = "✅"
                                            with open('kvant.json', 'w') as file:
                                                json.dump(data, file, indent=4)
                                            kv.append(k)
                                            id[k] = i
                                            e = 1
                                except:
                                    pass            
                        except:
                            pass    
                    r = ""
                    
                    with open('kvant.json', 'r') as file:
                        data = json.load(file)
                    name = str(message.chat.first_name)
                    idtg = str(message.from_user.id)
                    rbr = {"fio": data[idtg]["fio"], "kvan": {"kv_spis": kv, "id": id}, "dop" : {"user" : "0"}}
                    data[idtg] = rbr
                    with open('kvant.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    r = ""
                    for k in data[idtg]["kvan"]["kv_spis"]:
                        idtg_uch =  data[idtg]["kvan"]["id"][k]
                        for d in data[idtg_uch]["kvan"][k]["ras"]:
                            r += d + "\n" + data[idtg_uch]["kvan"][k]["ras"][d]["ras_str"] + "\n"
                        
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Мои квантумы👩‍🏫')
                    btn2 = types.KeyboardButton('Найти квантум📅')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
            <i><b>Информация📜</b></i>

<b>ФИО: {data[idtg]["fio"]}</b>🙍‍♂
<b>Ваше расписание:</b>

<b>{r}</b>


        <i>Нажмите на кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu)
            def regis1(message):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Ученик🙍‍♂':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
            <i><b>Регистрация</b></i>
<b>Введите своё Имя и Фамилию</b>
<i>Пример: Иван Иванов</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, regis2)
                    
                elif message.text == 'Учитель👩‍🏫':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
            <i><b>Регистрация</b></i>
<b>Введите пожалуйста код учителя:</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, regis3)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Ученик🙍‍♂')
                    btn2 = types.KeyboardButton('Учитель👩‍🏫')
                    markup.add(btn1, btn2)
                    bot.send_photo(message.chat.id, file, f'''
            <i><b>Регистрация</b></i>
<b>Ваши данные отсутствуют в базе данных! Для этого просим пройти регистрацию!</b>

<b>Кто вы?</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, regis1)
            def regis2(message):
                with open('uch.json', 'r') as file:
                    bd = json.load(file)
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                e = 2
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Ученик🙍‍♂')
                    btn2 = types.KeyboardButton('Учитель👩‍🏫')
                    markup.add(btn1, btn2)
                    file = open("image.png", "rb")
                    bot.send_photo(message.chat.id, file, f'''
            <i><b>Регистрация</b></i>
<b>Ваши данные отсутствуют в базе данных! Для этого просим пройти регистрацию!</b>

<b>Кто вы?</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, regis1)
                else:
                    e = 2
                    kv = []
                    id = {}
                    for i in data:
                        try:
                            for k in data[i]["kvan"]:
                                try:
                                    for l in data[i]["kvan"][k]["ludi"]:
                                        if message.text == l:
                                            kv.append(k)
                                            id[k] = i
                                            e = 1
                                except:
                                    pass            
                        except:
                            pass    
                    if e != 1:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                    <i><b>ОШИБКА!</b></i>
        <b>Введите своё Имя и Фамилию</b>
        <i>Пример: Иван Иванов</i>
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, regis2)       
                    elif e == 1:
                        with open('kvant.json', 'r') as file:
                            data = json.load(file)
                        name = str(message.chat.first_name)
                        idtg = str(message.from_user.id)
                        rbr = {"fio": message.text, "kvan": {"kv_spis": kv, "id": id}, "dop" : {"user" : "0"}}
                        data[idtg] = rbr
                        with open('kvant.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        bot.send_message(message.chat.id, f'''
                <b>Спасибо за регистрацию!</b>
        <i>{message.text} нажмите на кнопку "Назад👈🏻" чтобы прейти в главное меню!</i>
                        ''', parse_mode='HTML')
                        bot.register_next_step_handler(message, start)




            def regis3(message):
                with open('uch.json', 'r') as file:
                    bd = json.load(file)
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Ученик🙍‍♂')
                    btn2 = types.KeyboardButton('Учитель👩‍🏫')
                    markup.add(btn1, btn2)
                    file = open("image.png", "rb")
                    bot.send_photo(message.chat.id, file, f'''
            <i><b>Регистрация</b></i>
<b>Ваши данные отсутствуют в базе данных! Для этого просим пройти регистрацию!</b>

<b>Кто вы?</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, regis1)
                elif message.text in bd["id"]:
                    for i in bd["id"]:
                        if message.text == i:
                            with open('kvant.json', 'r') as file:
                                data = json.load(file)
                            name = str(message.chat.first_name)
                            idtg = str(message.from_user.id)
                            rbr = {"fio": bd["id"][i], "kvan": {}, "dop" : {"user" : "1", "name": message.from_user.username}}
                            data[idtg] = rbr
                            with open('kvant.json', 'w') as file:
                                json.dump(data, file, indent=4)
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                            btn1 = types.KeyboardButton('Назад👈🏻')
                            markup.add(btn1)
                            bot.send_message(message.chat.id, f'''
            <b>Спасибо за регистрацию!</b>
    <i>{bd["id"][i]} нажмите на кнопку "Назад👈🏻" чтобы прейти в главное меню!</i>
                            ''',  reply_markup=markup, parse_mode='HTML')
                            bot.register_next_step_handler(message, start)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
            <i><b>ОШИБКА!</b></i>
<b>Введите пожалуйста код учителя:</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, regis3)






            def menu(message):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Мои квантумы👩‍🏫':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    for i in data[idtg]["kvan"]["kv_spis"]:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    btn5 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn5)
                    bot.send_message(message.chat.id, f'''
        <i><b>Мои квантумы👩‍🏫</b></i>
<b>Ваши квантумы:</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_mk)
                elif message.text == 'Найти квантум📅':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Найти по типу')
                    markup.add(btn1)
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn2)
                    bot.send_message(message.chat.id, f'''
        <i><b>Найти квантум📅</b></i>

<b>Выберите тип поиска:</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_nk)

            def menu_nk(message):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    e = 2
                    kv = []
                    id = {}
                    for i in data:
                        try:
                            for k in data[i]["kvan"]:
                                try:
                                    for l in data[i]["kvan"][k]["ludi"]:
                                        if data[idtg]["fio"] == l:
                                            kv.append(k)
                                            id[k] = i
                                            e = 1
                                except:
                                    pass            
                        except:
                            pass    
                    r = ""
                    
                    with open('kvant.json', 'r') as file:
                        data = json.load(file)
                    name = str(message.chat.first_name)
                    idtg = str(message.from_user.id)
                    rbr = {"fio": data[idtg]["fio"], "kvan": {"kv_spis": kv, "id": id}, "dop" : {"user" : "0"}}
                    data[idtg] = rbr
                    with open('kvant.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    r = ""
                    for k in data[idtg]["kvan"]["kv_spis"]:
                        idtg_uch =  data[idtg]["kvan"]["id"][k]
                        for d in data[idtg_uch]["kvan"][k]["ras"]:
                            r += d + "\n" + data[idtg_uch]["kvan"][k]["ras"][d]["ras_str"] + "\n"
                        
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Мои квантумы👩‍🏫')
                    btn2 = types.KeyboardButton('Найти квантум📅')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
            <i><b>Информация📜</b></i>

<b>ФИО: {data[idtg]["fio"]}</b>🙍‍♂
<b>Ваше расписание:</b>

<b>{r}</b>


        <i>Нажмите на кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    
                    bot.register_next_step_handler(message, menu)
                elif message.text == 'Найти по типу':
                    kvantum = ["Кибербезопасность", "IT-КВАНТУМ", "Компьютерная грамотность", "Олимпиадная подготовка", "АЭРОквантум",  "БИОквантум", "НАНОквантум", "ПромРобо", "КВАНТОшахматы", "ЭНЕРДЖИквантум", "ХайТек", "Креативное программирование", "АвтоДело", "Технический английский", "Проектное управление", "Иностранный язык", "Финансовая культура", "Фотошкола"]
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn2)
                    for i in kvantum:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Найти по типу')
                    markup.add(btn1)
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn2)
                    bot.send_message(message.chat.id, f'''
        <i><b>Найти квантум📅</b></i>

<b>Выберите тип квантума:</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_nk_poiskT)
            def menu_nk_poiskT(message):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                kvantum = ["Кибербезопасность", "IT-КВАНТУМ", "Компьютерная грамотность", "Олимпиадная подготовка", "АЭРОквантум",  "БИОквантум", "НАНОквантум", "ПромРобо", "КВАНТОшахматы", "ЭНЕРДЖИквантум", "ХайТек", "Креативное программирование", "АвтоДело", "Технический английский", "Проектное управление", "Иностранный язык", "Финансовая культура", "Фотошкола"]
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Найти по типу')
                    markup.add(btn1)
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn2)
                    bot.send_message(message.chat.id, f'''
        <i><b>Найти квантум📅</b></i>

<b>Выберите тип поиска:</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_nk)
                elif message.text == 'Назад👈🏻':



            def menu_mk(message):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    e = 2
                    kv = []
                    id = {}
                    for i in data:
                        try:
                            for k in data[i]["kvan"]:
                                try:
                                    for l in data[i]["kvan"][k]["ludi"]:
                                        if data[idtg]["fio"] == l:
                                            kv.append(k)
                                            id[k] = i
                                            e = 1
                                except:
                                    pass            
                        except:
                            pass    
                    r = ""
                    
                    with open('kvant.json', 'r') as file:
                        data = json.load(file)
                    name = str(message.chat.first_name)
                    idtg = str(message.from_user.id)
                    rbr = {"fio": data[idtg]["fio"], "kvan": {"kv_spis": kv, "id": id}, "dop" : {"user" : "0"}}
                    data[idtg] = rbr
                    with open('kvant.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    r = ""
                    for k in data[idtg]["kvan"]["kv_spis"]:
                        idtg_uch =  data[idtg]["kvan"]["id"][k]
                        for d in data[idtg_uch]["kvan"][k]["ras"]:
                            r += d + "\n" + data[idtg_uch]["kvan"][k]["ras"][d]["ras_str"] + "\n"
                        
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Мои квантумы👩‍🏫')
                    btn2 = types.KeyboardButton('Найти квантум📅')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
            <i><b>Информация📜</b></i>

<b>ФИО: {data[idtg]["fio"]}</b>🙍‍♂
<b>Ваше расписание:</b>

<b>{r}</b>


        <i>Нажмите на кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    
                    bot.register_next_step_handler(message, menu)
                else:
                    y = 0
                    for i in data[idtg]["kvan"]["kv_spis"]:
                        if message.text == i:
                            r = ""
                            k = "Не указан"
                            idtg_uch =  data[idtg]["kvan"]["id"][i]
                            for d in data[idtg_uch]["kvan"][i]["ras"]:
                                r += d + "\n" + data[idtg_uch]["kvan"][i]["ras"][d]["ras_str"] + "\n"
                                try:
                                    k = data[idtg_uch]["kvan"][i]["ras"][d]["kab"]
                                except:
                                    k = "Не указан"
                            name = data[idtg_uch]["dop"]["name"]
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                            btn1 = types.KeyboardButton('Назад👈🏻')
                            markup.add(btn1)
                            bot.send_message(message.chat.id, f'''
                    <i><b>Информация📜</b></i>

        <b>Название: {message.text}</b>📰


<b>Расписание:</b>

<b>{r}</b>
                
<b>Кабинет - {k}</b>

<i>Связь с учителем - @{name}</i>

                <i>Выберите кнопку👇🏻</i>
                            ''',  reply_markup=markup, parse_mode='HTML')
                            k = i
                            y = 1
                            bot.register_next_step_handler(message, menu_mk_back)
                    if y == 0:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        for i in data[idtg]["kvan"]["kv_spis"]:
                            try:
                                btn1 = types.KeyboardButton(i)
                                markup.add(btn1)
                            except:
                                pass
                        btn5 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn5)
                        bot.send_message(message.chat.id, f'''
            <i><b>Мои квантумы👩‍🏫</b></i>
    <b>Ваши квантумы:</b>
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, menu_mk)
            def menu_mk_back(message):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                for i in data[idtg]["kvan"]["kv_spis"]:
                    try:
                        btn1 = types.KeyboardButton(i)
                        markup.add(btn1)
                    except:
                        pass
                btn5 = types.KeyboardButton('Назад👈🏻')
                markup.add(btn5)
                bot.send_message(message.chat.id, f'''
    <i><b>Мои квантумы👩‍🏫</b></i>
<b>Ваши квантумы:</b>
                ''',  reply_markup=markup, parse_mode='HTML')
                bot.register_next_step_handler(message, menu_mk)
            def menu_uch(message):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Квантумы👩‍🏫':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    for i in data[idtg]["kvan"]:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    btn4 = types.KeyboardButton('Создать квантум')
                    markup.add(btn4)
                    btn5 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn5)
                    bot.send_message(message.chat.id, f'''
        <i><b>Квантумы👩‍🏫</b></i>
<b>Ваши квантумы:</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv)
                if message.text == 'Admin':
                    with open('kvant.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Пароль: 
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_admin)
                


                def menu_admin(message):
                    with open('kvant.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    if message.text == 'Назад👈🏻':
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Квантумы👩‍🏫')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                    <i><b>Информация📜</b></i>

            <b>ФИО: {data[idtg]["fio"]}</b>🙍‍♂

            <i>Нажмите на кнопку👇🏻</i>
                        ''',  reply_markup=markup, parse_mode='HTML')
                        
                        bot.register_next_step_handler(message, menu_uch)
                    elif message.text == 'diradm':
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                        Скоро тут будет полная аналитика бота....
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, start)
                    elif message.text == 'sisadm1':
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Сохранить базу данных')
                        btn1 = types.KeyboardButton('Удалить базу данных')
                        btn1 = types.KeyboardButton('Режим разработки')
                        btn1 = types.KeyboardButton('Режим тестировки')
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                        Скоро тут будет полная аналитика бота....
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, menu_admin_adm)

















            def menu_uch_kv(message):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Квантумы👩‍🏫')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                <i><b>Информация📜</b></i>

        <b>ФИО: {data[idtg]["fio"]}</b>🙍‍♂

        <i>Нажмите на кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    
                    bot.register_next_step_handler(message, menu_uch)
                elif message.text == 'Создать квантум':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                <i><b>Создать квантум👩‍🏫</b></i>

        <b>Напишите название нового квантума:</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_dop)
                else:
                    y = 0
                    for i in data[idtg]["kvan"]:
                        if message.text == i:
                            
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                            btn1 = types.KeyboardButton('Расписание📅')
                            btn2 = types.KeyboardButton('Ученики🙍‍♂️')
                            btn3 = types.KeyboardButton('Описание квантума💬')
                            btn4 = types.KeyboardButton('Рассылка📤')
                            btn5 = types.KeyboardButton('Назад👈🏻')
                            markup.add(btn1, btn2, btn3, btn4, btn5)
                            bot.send_message(message.chat.id, f'''
                        <i><b>Информация📜</b></i>

                <b>Название: {message.text}</b>📰
                
                <b>Количество учеников: {len(data[idtg]["kvan"][i]["ludi"])}</b>🙍‍♂️

                <b>Описание квантума: {data[idtg]["kvan"][i]["dop"]["bio"]["text"]}</b>

                <i>Выберите кнопку👇🏻</i>
                            ''',  reply_markup=markup, parse_mode='HTML')
                            k = i
                            y = 1
                            bot.register_next_step_handler(message, menu_uch_kv_n, k)
                    if y == 0:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                        Я вас не понял(( Возвращайтесь обратно! 
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, menu_uch_kv_back)










            def menu_uch_kv_n(message, k):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    for i in data[idtg]["kvan"]:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    btn4 = types.KeyboardButton('Создать квантум')
                    markup.add(btn4)
                    btn5 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn5)
                    bot.send_message(message.chat.id, f'''
        <i><b>Квантумы👩‍🏫</b></i>
    <b>Ваши квантумы:</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv)
                elif message.text == "Описание квантума💬":
                    with open('kvant.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Тип квантума')
                    btn2 = types.KeyboardButton('О квантуме')
                    btn3 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                <i><b>Описание квантума💬</b></i>
        <b>Тип квантума: {data[idtg]["kvan"][k]["dop"]["bio"]["kv"]}</b>
        <b>О квантуме: 
        {data[idtg]["kvan"][k]["dop"]["bio"]["opis"]}</b>

        <i>Выберите кнопку чтобы изменить описание👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    
                    bot.register_next_step_handler(message, menu_uch_kv_n_ok, k)
                elif message.text == 'Расписание📅':
                    with open('kvant.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    for i in data[idtg]["kvan"][k]["ras"]:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    btn4 = types.KeyboardButton('Добавить день➕')
                    markup.add(btn4)
                    btn5 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn5)
                    bot.send_message(message.chat.id, f'''
        <i><b>Расписание📅</b></i>

    <i>*Нажмите на день чтобы изменить или добавить</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras, k)
                elif message.text == 'Ученики🙍‍♂️':
                    with open('kvant.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    u = ""
                    for i in data[idtg]["kvan"][k]["ludi"]:
                        u += i + " " + data[idtg]["kvan"][k]["ludi"][i] + "\n"
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Добавить➕')
                    btn2 = types.KeyboardButton('Удалить➖')
                    btn3 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                <i><b>Ученики🙍‍♂</b></i>

        Ваши ученики: 

<b>{u}</b>

        <i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_u, k)
                elif message.text == 'Рассылка📤':
                    with open('kvant.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                <i><b>Рассылка📤</b></i>

        <i>Введите текст рассылки:</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_rassilka, k)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Я вас не понял(( Возвращайтесь обратно! 
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_back)

            def menu_uch_kv_n_ok(message, k):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                            
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Расписание📅')
                    btn2 = types.KeyboardButton('Ученики🙍‍♂️')
                    btn3 = types.KeyboardButton('Описание квантума💬')
                    btn4 = types.KeyboardButton('Рассылка📤')
                    btn5 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(message.chat.id, f'''
                <i><b>Информация📜</b></i>

        <b>Название: {message.text}</b>📰
        
        <b>Количество учеников: {len(data[idtg]["kvan"][k]["ludi"])}</b>🙍‍♂️

        <b>Описание квантума: {data[idtg]["kvan"][k]["dop"]["bio"]["text"]}</b>
        <i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n, k)
                elif message.text == 'Тип квантума':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    kvantum = ["Кибербезопасность", "IT-КВАНТУМ", "Компьютерная грамотность", "Олимпиадная подготовка", "АЭРОквантум",  "БИОквантум", "НАНОквантум", "ПромРобо", "КВАНТОшахматы", "ЭНЕРДЖИквантум", "ХайТек", "Креативное программирование", "АвтоДело", "Технический английский", "Проектное управление", "Иностранный язык", "Финансовая культура", "Фотошкола"]
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn2)
                    for i in kvantum:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    
                    bot.send_message(message.chat.id, f'''
                    Выберите тип квантума:
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ok_tip, k)
                elif message.text == 'О квантуме':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn2)
                    bot.send_message(message.chat.id, f'''
                    Опишите свой для привлечения учеников!
            <i>Пример: Привет! Наш квантум создан для изучения насекомых! Если тебе это интерестно, добавляйся!</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ok_opis, k)
            
            def menu_uch_kv_n_ok_opis(message, k):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Тип квантума')
                    btn2 = types.KeyboardButton('О квантуме')
                    btn3 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                <i><b>Описание квантума💬</b></i>
        <b>Тип квантума: {data[idtg]["kvan"][k]["dop"]["bio"]["kv"]}</b>
        <b>О квантуме: 
        <i>{data[idtg]["kvan"][k]["dop"]["bio"]["opis"]}</i></b>

        <i>Выберите кнопку чтобы изменить описание👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    
                    bot.register_next_step_handler(message, menu_uch_kv_n_ok, k)
                else:
                    data[idtg]["kvan"][k]["dop"]["bio"]["opis"] = message.text
                    data[idtg]["kvan"][k]["dop"]["bio"]["text"] = "Добавлено"
                    with open('kvant.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Описание квантума изменено успешно! 
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ok_back, k)
            def menu_uch_kv_n_ok_tip(message, k):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                kvantum = ["Кибербезопасность", "IT-КВАНТУМ", "Компьютерная грамотность", "Олимпиадная подготовка", "АЭРОквантум",  "БИОквантум", "НАНОквантум", "ПромРобо", "КВАНТОшахматы", "ЭНЕРДЖИквантум", "ХайТек", "Креативное программирование", "АвтоДело", "Технический английский", "Проектное управление", "Иностранный язык", "Финансовая культура", "Фотошкола"]

                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Тип квантума')
                    btn2 = types.KeyboardButton('О квантуме')
                    btn3 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                <i><b>Описание квантума💬</b></i>
        <b>Тип квантума: {data[idtg]["kvan"][k]["dop"]["bio"]["kv"]}</b>
        <b>О квантуме: 
        <i>{data[idtg]["kvan"][k]["dop"]["bio"]["opis"]}</i></b>

        <i>Выберите кнопку чтобы изменить описание👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    
                    bot.register_next_step_handler(message, menu_uch_kv_n_ok, k)
                elif message.text in kvantum:
                    data[idtg]["kvan"][k]["dop"]["bio"]["kv"] = message.text
                    with open('kvant.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Тип квантума изменён успешно! 
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ok_back, k)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Тип квантума')
                    btn2 = types.KeyboardButton('О квантуме')
                    btn3 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                <i><b>Описание квантума💬</b></i>
        <b>Тип квантума: {data[idtg]["kvan"][k]["dop"]["bio"]["kv"]}</b>
        <b>О квантуме: 
        <i>{data[idtg]["kvan"][k]["dop"]["bio"]["opis"]}</i></b>

        <i>Выберите кнопку чтобы изменить описание👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    
                    bot.register_next_step_handler(message, menu_uch_kv_n_ok, k)
            def menu_uch_kv_n_ok_back(message,k):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                btn1 = types.KeyboardButton('Тип квантума')
                btn2 = types.KeyboardButton('О квантуме')
                btn3 = types.KeyboardButton('Назад👈🏻')
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, f'''
            <i><b>Описание квантума💬</b></i>
    <b>Тип квантума: {data[idtg]["kvan"][k]["dop"]["bio"]["kv"]}</b>
    <b>О квантуме: 
    <i>{data[idtg]["kvan"][k]["dop"]["bio"]["opis"]}</i></b>

    <i>Выберите кнопку чтобы изменить описание👇🏻</i>
                ''',  reply_markup=markup, parse_mode='HTML')
                
                bot.register_next_step_handler(message, menu_uch_kv_n_ok, k)
            def menu_uch_kv_n_rassilka(message, k):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                            
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Расписание📅')
                    btn2 = types.KeyboardButton('Ученики🙍‍♂️')
                    btn3 = types.KeyboardButton('Описание квантума💬')
                    btn4 = types.KeyboardButton('Рассылка📤')
                    btn5 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(message.chat.id, f'''
                <i><b>Информация📜</b></i>

        <b>Название: {message.text}</b>📰
        
        <b>Количество учеников: {len(data[idtg]["kvan"][k]["ludi"])}</b>🙍‍♂️

        <b>Описание квантума: {data[idtg]["kvan"][k]["dop"]["bio"]["text"]}</b>
        <i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n, k) 
                else:
                    for i in data:
                        if data[i]["fio"] in data[idtg]["kvan"][k]["ludi"]:
                            bot.send_message(i, message.text, parse_mode='HTML')
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Готово! Сообщения отправлены!
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_back)









            def menu_uch_kv_dop(message):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    for i in data[idtg]["kvan"]:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    btn4 = types.KeyboardButton('Создать квантум')
                    markup.add(btn4)
                    btn5 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn5)
                    bot.send_message(message.chat.id, f'''
        <i><b>Квантумы👩‍🏫</b></i>
    <b>Ваши квантумы:</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv)
                elif message.text == 'Создать квантум':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    for i in data[idtg]["kvan"]:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    btn4 = types.KeyboardButton('Создать квантум')
                    markup.add(btn4)
                    btn5 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn5)
                    bot.send_message(message.chat.id, f'''
        <i><b>Квантумы👩‍🏫</b></i>
    <b>Ваши квантумы:</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv)
                else:
                    with open('kvant.json', 'r') as file:
                        data = json.load(file)
                    rbr = {"ras" : {}, "ludi" : {}, "dop" : {"bio": {"text": "Не заполнено!", "kv": "❌", "opis": "❌"}}}
                    data[idtg]["kvan"][message.text] = rbr
                    with open('kvant.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    <i>Квантум успешно создан</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_back)










            
            def menu_uch_kv_n_u(message, k):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Расписание📅')
                    btn2 = types.KeyboardButton('Ученики🙍‍♂️')
                    btn3 = types.KeyboardButton('Описание квантума💬')
                    btn4 = types.KeyboardButton('Рассылка📤')
                    btn5 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(message.chat.id, f'''
                <i><b>Информация📜</b></i>

        <b>Название: {message.text}</b>📰
        
        <b>Количество учеников: {len(data[idtg]["kvan"][k]["ludi"])}</b>🙍‍♂️

        <b>Описание квантума: {data[idtg]["kvan"][k]["dop"]["bio"]["text"]}</b>

        <i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n, k)
                elif message.text == 'Добавить➕':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    <b>Напишите Имя и Фамилию</b>
                    <i>Пример: Иван Петров</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_u_dop, k)
                elif message.text == 'Удалить➖':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    for i in data[idtg]["kvan"][k]["ludi"]:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    btn5 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn5)
                    bot.send_message(message.chat.id, f'''
                    <b>Выберите человека которого хотите удалить:</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_u_del, k)

                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Я вас не понял(( Возвращайтесь обратно! 
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_back)

            def menu_uch_kv_n_u_del(message, k):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    u = ""
                    for i in data[idtg]["kvan"][k]["ludi"]:
                        u += i + " " + data[idtg]["kvan"][k]["ludi"][i] + "\n"
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Добавить➕')
                    btn2 = types.KeyboardButton('Удалить➖')
                    btn3 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                <i><b>Ученики🙍‍♂️</b></i>

        Ваши ученики: 

<b>{u}</b>

        <i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_u, k)
                else:
                    try:
                        with open('kvant.json', 'r') as file:
                            data = json.load(file)
                        del data[idtg]["kvan"][k]["ludi"][message.text]
                        with open('kvant.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                        Ученик успешно удалён!
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, menu_uch_kv_n_u_back, k)
                    except:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                        Ученика нет в базе! Попробуйте ёщё раз!
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, menu_uch_kv_n_u_back, k)

            def menu_uch_kv_n_u_dop(message, k):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    u = ""
                    for i in data[idtg]["kvan"][k]["ludi"]:
                        u += i + " " + data[idtg]["kvan"][k]["ludi"][i] + "\n"
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Добавить➕')
                    btn2 = types.KeyboardButton('Удалить➖')
                    btn3 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                <i><b>Ученики🙍‍♂️</b></i>

        Ваши ученики: 

<b>{u}</b>

        <i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_u, k)
                else:
                    with open('uch.json', 'r') as file:
                        bd = json.load(file)
                    u = bd["id"].values()
                    if message.text not in u and message.text not in data[idtg]["kvan"][k]["ludi"]:
                        with open('kvant.json', 'r') as file:
                            data = json.load(file)
                        data[idtg]["kvan"][k]["ludi"][message.text] = "❌"
                        with open('kvant.json', 'w') as file:
                            json.dump(data, file, indent=4)
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                        Ученик успешно добавлен!
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, menu_uch_kv_n_u_back, k)
                    else:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                        <b>ОШИБКА!</b>
                <b>Напишите Имя и Фамилию</b>
                <i>Пример: Иван Петров</i>
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, menu_uch_kv_n_u_dop, k)

            def menu_uch_kv_n_u_back(message, k):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                u = ""
                for i in data[idtg]["kvan"][k]["ludi"]:
                    u += i + " " + data[idtg]["kvan"][k]["ludi"][i] + "\n"
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                btn1 = types.KeyboardButton('Добавить➕')
                btn2 = types.KeyboardButton('Удалить➖')
                btn3 = types.KeyboardButton('Назад👈🏻')
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, f'''
            <i><b>Ученики🙍‍♂️</b></i>

        Ваши ученики: 

<b>{u}</b>

        <i>Выберите кнопку👇🏻</i>
                ''',  reply_markup=markup, parse_mode='HTML')
                bot.register_next_step_handler(message, menu_uch_kv_n_u, k)

            def menu_uch_kv_n_ras(message, k):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Расписание📅')
                    btn2 = types.KeyboardButton('Ученики🙍‍♂️')
                    btn3 = types.KeyboardButton('Описание квантума💬')
                    btn4 = types.KeyboardButton('Рассылка📤')
                    btn5 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(message.chat.id, f'''
                <i><b>Информация📜</b></i>

        <b>Название: {k}</b>📰
        
        <b>Количество учеников: {len(data[idtg]["kvan"][k]["ludi"])}</b>🙍‍♂️

        <b>Описание квантума: {data[idtg]["kvan"][k]["dop"]["bio"]["text"]}</b>

        <i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n, k)
                elif message.text == 'Добавить день➕':
                    d = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    for i in d:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn2)
                    bot.send_message(message.chat.id, f'''
                <i><b>Добавить день➕</b></i>

        <b>Какой день вы хотите добавить?</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    d = message.text
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras_n_dop, k, d)
                else:
                    y = 0
                    for i in data[idtg]["kvan"][k]["ras"]:
                        if message.text == i:
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                            btn1 = types.KeyboardButton('Добавить новое расписание📅')
                            btn2= types.KeyboardButton('Добавить кабинет🏛')
                            btn3 = types.KeyboardButton('Удалить день❌')
                            btn4 = types.KeyboardButton('Назад👈🏻')
                            markup.add(btn1, btn2, btn3, btn4)
                            bot.send_message(message.chat.id, f'''
                <i><b>{message.text}</b></i>
        <b>Расписание: 
        {data[idtg]["kvan"][k]["ras"][message.text]["ras_str"]}</b>
        <i>Выберите кнопку👇🏻</i>
                            ''',  reply_markup=markup, parse_mode='HTML')
                            d = i
                            y = 1
                            bot.register_next_step_handler(message, menu_uch_kv_n_ras_n, k, d)
                    if y == 0:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                        Я вас не понял(( Возвращайтесь обратно! 
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, menu_uch_kv_back)
                









            def menu_uch_kv_n_ras_n(message, k, d):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    with open('kvant.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    for i in data[idtg]["kvan"][k]["ras"]:
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    btn4 = types.KeyboardButton('Добавить день➕')
                    markup.add(btn4)
                    btn5 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn5)
                    bot.send_message(message.chat.id, f'''
        <i><b>Расписание📅</b></i>

    <i>*Нажмите на день чтобы изменить или добавить</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras, k)
                elif message.text == 'Добавить новое расписание📅':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Приступить')
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
                    <b>Вы точно хотите приступить к запалнению расписания?</b>
                    <b>Старое расписание будет удалено!</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras_n_dopras, k, d)
                elif message.text == 'Удалить день❌':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    btn2 = types.KeyboardButton('Удалить❌')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
        <i><b>Удалить день❌</b></i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras_n_dop, k, d)
                elif message.text == 'Добавить кабинет🏛':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 5)
                    for i in range(1, 31):
                        try:
                            btn1 = types.KeyboardButton(i)
                            markup.add(btn1)
                        except:
                            pass
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn2)
                    bot.send_message(message.chat.id, f'''
                <i><b>Добавить кабинет🏛</b></i>

        <b>Какой кабинет вы хотите добавить?</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras_n_dopkab, k, d)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Я вас не понял(( Возвращайтесь обратно! 
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_back)

            def menu_uch_kv_n_ras_n_dopkab(message, k, d):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Добавить новое расписание📅')
                    btn2= types.KeyboardButton('Добавить кабинет🏛')
                    btn3 = types.KeyboardButton('Удалить день❌')
                    btn4 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3, btn4)
                    bot.send_message(message.chat.id, f'''
        <i><b>{d}</b></i>
<b>Расписание: 
{data[idtg]["kvan"][k]["ras"][d]["ras_str"]}</b>
<i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras_n, k, d)
                else:
                    x = 1
                    for i in range(1, 31):
                        try:
                            if int(message.text) == i:
                                with open('kvant.json', 'r') as file:
                                    data = json.load(file) 
                                data[idtg]["kvan"][k]["ras"][d]["kab"] = message.text
                                with open('kvant.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                                btn1 = types.KeyboardButton('Назад👈🏻')
                                markup.add(btn1)
                                bot.send_message(message.chat.id, f'''
            <i>День успешно добавлен!</i>
                                ''',  reply_markup=markup, parse_mode='HTML')
                                bot.register_next_step_handler(message, menu_uch_kv_n_ras_back, k, d)
                                x = 2
                                break
                                
                        except:
                            pass
                    if x == 1:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
        <i>Ошибка!</i>
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, menu_uch_kv_n_ras_back, k, d)

            def menu_uch_kv_n_ras_n_dop(message, k, d):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                print(message, k, d)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Добавить новое расписание📅')
                    btn2= types.KeyboardButton('Добавить кабинет🏛')
                    btn3 = types.KeyboardButton('Удалить день❌')
                    btn4 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3, btn4)
                    bot.send_message(message.chat.id, f'''
        <i><b>{d}</b></i>
<b>Расписание: 
{data[idtg]["kvan"][k]["ras"][d]["ras_str"]}</b>
<i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras_n, k, d)
                

                
                elif message.text in ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]:
                    with open('kvant.json', 'r') as file:
                        data = json.load(file) 
                    data[idtg]["kvan"][k]["ras"][message.text] = {"ras_str" : "", "ras_bd": []}
                    with open('kvant.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
<i>День успешно добавлен!</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    d = message.text
                    
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras_back, k, d)
                elif message.text == 'Удалить❌':
                    with open('kvant.json', 'r') as file:
                        data = json.load(file)
                    del data[idtg]["kvan"][k]["ras"][d]
                    with open('kvant.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
<i>День успешно удалён!</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras_back, k, d)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Я вас не понял(( Возвращайтесь обратно! 
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras_back, k, d)



            def menu_uch_kv_n_ras_n_dopras(message, k, d):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Добавить новое расписание📅')
                    btn2= types.KeyboardButton('Добавить кабинет🏛')
                    btn3 = types.KeyboardButton('Удалить день❌')
                    btn4 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3, btn4)
                    bot.send_message(message.chat.id, f'''
        <i><b>{d}</b></i>
<b>Расписание: 
{data[idtg]["kvan"][k]["ras"][d]["ras_str"]}</b>
<i>Выберите кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras_n, k, d)
                else:
                    try:
                        bot.send_message(message.chat.id, f'''
            <i><b>Добавление расписания📅</b></i>
    <b>Напишите время начала и конец урокa</b>
    <i>Пример: 8.00-8.45</i>
                        ''', parse_mode='HTML')
                        bot.register_next_step_handler(message, menu_uch_kv_n_ras_n_dop_n, k, d)
                    except:
                        pass
            
            def menu_uch_kv_n_ras_n_dop_n(message, k, d):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                try:
                    try:
                        pas1 = message.text.split("-")
                        pas = []
                        for i in pas1:
                            i = i.split(".")
                            pas.append(i[0])
                            pas.append(i[1])
                        p = 1
                    except:
                        p = 0
                    if p == 0:
                        reply_markup = types.ReplyKeyboardRemove()
                        bot.send_message(message.chat.id, f'''
                <i><b>ОШИБКА!</b></i>
        <b>Напишите время начала урока и конец</b>
        <i>Пример: 8.00-8.45</i>
                        ''', parse_mode='HTML')
                        bot.register_next_step_handler(message, menu_uch_kv_n_ras_n_dop_n, k, d)
                    elif int(pas[0]) >= 25 or int(pas[2]) >= 25 or int(pas[1]) >= 60 or int(pas[3]) >= 60:
                        reply_markup = types.ReplyKeyboardRemove()
                        bot.send_message(message.chat.id, f'''
                <i><b>ОШИБКА!</b></i>
        <b>Напишите время начала урока и конец</b>
        <i>Пример: 8.00-8.45</i>
                        ''', parse_mode='HTML')
                        bot.register_next_step_handler(message, menu_uch_kv_n_ras_n_dop_n, k, d)
                    else:
                        ras_str = ""
                        ras_bd = []
                        ras_str = ras_str + k + ": " + message.text + "\n"
                        ras_bd.append(message.text)
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Завершить заполнение✅')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
            <i><b>Добавление расписания📅</b></i>
    <b>Напишите время начала и конец перемены</b>
    <i>Пример: 8.00-8.45</i>
                        ''', parse_mode='HTML',  reply_markup=markup)
                        bot.register_next_step_handler(message, ras_peremen, k, d, ras_str, ras_bd)
                except:
                    reply_markup = types.ReplyKeyboardRemove()
                    bot.send_message(message.chat.id, f'''
                <i><b>ОШИБКА!</b></i>
        <b>Напишите время начала урока и конец</b>
        <i>Пример: 8.00-8.45</i>
                    ''', parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras_n_dop_n, k, d)
            def ras_peremen(message, k, d, ras_str, ras_bd):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Завершить заполнение✅':
                    data[idtg]["kvan"][k]["ras"][d]["ras_bd"] = ras_bd
                    data[idtg]["kvan"][k]["ras"][d]["ras_str"] = ras_str
                    with open('kvant.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                <i><b>Добавление расписания📅</b></i>
<b>Ваше новое расписание:</b>
<b>{ras_str}</b>
                    ''', parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras_back, k, d)
                else:
                    try:
                        try:
                            pas1 = message.text.split("-")
                            pas = []
                            for i in pas1:
                                i = i.split(".")
                                pas.append(i[0])
                                pas.append(i[1])
                            p = 1
                        except:
                            p = 0
                        if p == 0:
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                            btn1 = types.KeyboardButton('Завершить заполнение✅')
                            markup.add(btn1)
                            bot.send_message(message.chat.id, f'''
                <i><b>Добавление расписания📅</b></i>
        <b>Напишите время начала и конец перемены</b>
        <i>Пример: 8.00-8.45</i>
                            ''', parse_mode='HTML',  reply_markup=markup)
                            bot.register_next_step_handler(message, ras_peremen, k, d, ras_str, ras_bd)
                        elif int(pas[0]) >= 25 or int(pas[2]) >= 25 or int(pas[1]) >= 60 or int(pas[3]) >= 60:
                            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                            btn1 = types.KeyboardButton('Завершить заполнение✅')
                            markup.add(btn1)
                            bot.send_message(message.chat.id, f'''
                <i><b>Добавление расписания📅</b></i>
        <b>Напишите время начала и конец перемены</b>
        <i>Пример: 8.00-8.45</i>
                            ''', parse_mode='HTML',  reply_markup=markup)
                            bot.register_next_step_handler(message, ras_peremen, k, d, ras_str, ras_bd)
                        else:
                            reply_markup = types.ReplyKeyboardRemove()
                            ras_str = ras_str + "Перемена" + ": " + message.text + "\n"
                            ras_bd.append(message.text)
                            bot.send_message(message.chat.id, f'''
                <i><b>Добавление расписания📅</b></i>
        <b>Напишите время начала и конец урока</b>
        <i>Пример: 8.00-8.45</i>
                            ''', parse_mode='HTML')
                            bot.register_next_step_handler(message, ras_urok, k, d, ras_str, ras_bd)
                    except:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Завершить заполнение✅')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
            <i><b>Добавление расписания📅</b></i>
    <b>Напишите время начала и конец перемены</b>
    <i>Пример: 8.00-8.45</i>
                        ''', parse_mode='HTML',  reply_markup=markup)
                        bot.register_next_step_handler(message, ras_peremen, k, d, ras_str, ras_bd)
                

            def ras_urok(message, k, d, ras_str, ras_bd):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                try:
                    try:
                        pas1 = message.text.split("-")
                        pas = []
                        for i in pas1:
                            i = i.split(".")
                            pas.append(i[0])
                            pas.append(i[1])
                        p = 1
                    except:
                        p = 0
                    if p == 0:
                        reply_markup = types.ReplyKeyboardRemove()
                        bot.send_message(message.chat.id, f'''
                <i><b>ОШИБКА!</b></i>
        <b>Напишите время начала урока и конец</b>
        <i>Пример: 8.00-8.45</i>
                        ''', parse_mode='HTML')
                        bot.register_next_step_handler(message, menu_uch_kv_n_ras_n_dop_n, k, d)
                    elif int(pas[0]) >= 25 or int(pas[2]) >= 25 or int(pas[1]) >= 60 or int(pas[3]) >= 60:
                        reply_markup = types.ReplyKeyboardRemove()
                        bot.send_message(message.chat.id, f'''
                <i><b>ОШИБКА!</b></i>
        <b>Напишите время начала урока и конец</b>
        <i>Пример: 8.00-8.45</i>
                        ''', parse_mode='HTML')
                        bot.register_next_step_handler(message, menu_uch_kv_n_ras_n_dop_n, k, d)
                    else:
                        ras_str = ras_str + k + ": " + message.text + "\n"
                        ras_bd.append(message.text)
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Завершить заполнение✅')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
            <i><b>Добавление расписания📅</b></i>
    <b>Напишите время начала и конец перемены</b>
    <i>Пример: 8.00-8.45</i>
                        ''', parse_mode='HTML',  reply_markup=markup)
                        bot.register_next_step_handler(message, ras_peremen, k, d, ras_str, ras_bd)
                except:
                    reply_markup = types.ReplyKeyboardRemove()
                    bot.send_message(message.chat.id, f'''
                <i><b>ОШИБКА!</b></i>
        <b>Напишите время начала урока и конец</b>
        <i>Пример: 8.00-8.45</i>
                    ''', parse_mode='HTML')
                    bot.register_next_step_handler(message, menu_uch_kv_n_ras_n_dop_n, k, d)
            def menu_uch_kv_n_ras_back(message, k, d):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                try:
                    ras_str = data[idtg]["kvan"][k]["ras"][d]["ras_str"]
                except:
                    ras_str = ""
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                for i in data[idtg]["kvan"][k]["ras"]:
                    try:
                        btn1 = types.KeyboardButton(i)
                        markup.add(btn1)
                    except:
                        pass
                btn4 = types.KeyboardButton('Добавить день➕')
                markup.add(btn4)
                btn5 = types.KeyboardButton('Назад👈🏻')
                markup.add(btn5)
                bot.send_message(message.chat.id, f'''
        <i><b>Расписание📅</b></i>

<i>*Нажмите на день чтобы изменить или добавить</i>
                ''',  reply_markup=markup, parse_mode='HTML')
                bot.register_next_step_handler(message, menu_uch_kv_n_ras, k)





            def menu_uch_kv_back(message):
                with open('kvant.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                for i in data[idtg]["kvan"]:
                    try:
                        btn1 = types.KeyboardButton(i)
                        markup.add(btn1)
                    except:
                        pass
                btn4 = types.KeyboardButton('Создать квантум')
                markup.add(btn4)
                btn5 = types.KeyboardButton('Назад👈🏻')
                markup.add(btn5)
                bot.send_message(message.chat.id, f'''
    <i><b>Квантумы👩‍🏫</b></i>
<b>Ваши квантумы:</b>
                ''',  reply_markup=markup, parse_mode='HTML')
                bot.register_next_step_handler(message, menu_uch_kv)
            @bot.message_handler(content_types=["text"])
            def osh(message):
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                btn1 = types.KeyboardButton('/start')
                markup.add(btn1)
                bot.send_message(message.chat.id, f"Я вас не понял! Нажмите: /start", reply_markup=markup)
            bot.polling(none_stop=True, timeout=200)
        else:
            pass
main()