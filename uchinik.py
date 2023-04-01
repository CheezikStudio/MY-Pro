# 5608361983:AAHErlMkMaGAQ1iqaRFR3EpkTPBiV-oTU4I - Ученик
import telebot 
import json
from telebot import types
import random
import config
def main():
    while True:
        if True:
            bot = telebot.TeleBot('5608361983:AAHErlMkMaGAQ1iqaRFR3EpkTPBiV-oTU4I')
            @bot.message_handler(commands=["start"])
            def start(message, res=False):
                with open('uchenik.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == "/start" or message.text == "/menu":
                    if idtg not in data:
                        bot.send_message(message.chat.id, f'''
<i><b>Регистрация</b></i>

<b>Введите своё Имя и Фамилию</b>
<i>Пример: Иван Иванов</i>
                        ''', parse_mode='HTML')
                        bot.register_next_step_handler(message, regis)
                    else:
                        markup = types.InlineKeyboardMarkup(row_width = 1)
                        btn1 = types.InlineKeyboardButton(text="Мои квантумы👩‍🏫", callback_data="moikvant")
                        btn2 = types.InlineKeyboardButton(text="Найти квантум📅", callback_data="find")
                        markup.add(btn1, btn2)
                        r = 0
                        bot.send_message(message.chat.id, config.menu_uchenik(idtg, data, r), parse_mode='HTML')

            def regis(message):
                with open('logins.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text in data["uchenik"]:
                    k = data["uchenik"][message.text]["kvant"]
                    e = 1  
                if e != 1:
                    bot.send_message(message.chat.id, f'''
<i><b>ОШИБКА!</b></i>

<b>Введите своё Имя и Фамилию</b>
<i>Пример: Иван Иванов</i>
                    ''', parse_mode='HTML')
                    bot.register_next_step_handler(message, regis)
                elif e == 1:
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardButton(text="В меню📅", callback_data="menu")
                    markup.add(btn1)
                    with open('uchenik.json', 'r') as file:
                        data = json.load(file)
                    name = str(message.chat.first_name)
                    idtg = str(message.from_user.id)
                    rbr = {"fio": message.text, "kvan": k, "dop" : {}}
                    data[idtg] = rbr
                    with open('kvant.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    bot.send_message(message.chat.id, f'''
<b>Спасибо за регистрацию!</b>

<i>{message.text} нажимай на кнопку и переходи в меню!</i>
                    ''', parse_mode='HTML', reply_markup=markup)
                    bot.register_next_step_handler(message, start)
            @bot.message_handler(content_types=["text"])
            def menu(message, res=False):
                pass
            @bot.callback_query_handler(func=lambda call: True)
            def call_menu(call):
                pass
            pass
            bot.polling(none_stop=True)
        else:
            pass
main()