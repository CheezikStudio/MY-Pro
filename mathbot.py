import telebot 
import json
from telebot import types
import random
from math import *
def main():
    while True:
        if True:
            bot = telebot.TeleBot('5518598503:AAEQW_qciU_Xw9SWMxKBQ7csucn0WprQ3A4')
            @bot.message_handler(commands=["start", "menu"])
            def start(message, res=False):
                with open('mathbotbd.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if idtg not in data:
                    people = {"fio": message.from_user.first_name, "sub": "✅", "dop": {}}
                    data[idtg] = people
                    with open('mathbotbd.json', 'w') as file:
                        json.dump(data, file, indent=4)
                if message.text == "/start" or message.text == "/menu":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Алгебра')
                    btn2 = types.KeyboardButton('Геометрия')
                    btn3 = types.KeyboardButton('Информация')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                <i><b>Информация📜</b></i>

        <b><i>Статистика бота:</i></b>
        🙍‍♂<b>Пользуются сервисом: {len(data)}</b>
        
        <i>Выберите тип👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
            @bot.message_handler(content_types=["text"])
            def menu(message, res=False):
                with open('mathbotbd.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == "Алгебра":
                    # {'НОД': 'nod', 'Факториал': 'fak', 'Корень': 'kor', 'Степень': 'step', 'Куб': 'kub', 'Сложение': 'sloz', 'Вычитание': 'vuch', 'Деление': 'del', 'Умножение': 'ymnoz'}
                    
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardButton(text="Калькулятор", callback_data="kalkulatora")
                    btn2 = types.InlineKeyboardButton(text="Формулы", callback_data="formulya")
                    btn3 = types.InlineKeyboardButton(text="Правила", callback_data="pravilaa")
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                <i><b>Алгебра➕</b></i>

        <i>Выберите действие👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                elif message.text == "Геометрия":
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardButton(text="Калькулятор", callback_data="kalkulatorg")
                    btn2 = types.InlineKeyboardButton(text="Формулы", callback_data="formulyg")
                    btn3 = types.InlineKeyboardButton(text="Правила", callback_data="pravilag")
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                <i><b>Геометрия🔷</b></i>

        <i>Выберите действие👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                elif message.text == "Информация":
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardButton(text="Наша студия", url="https://vk.com/whitedevstudio")
                    btn2 = types.InlineKeyboardButton(text="В главное меню", callback_data="gm")
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
        Бот сделан студией WhiteDevStudio
        Версия 1.1

        По всем вопросам: @devinpython
                    ''',  reply_markup=markup, parse_mode='HTML')
                else:
                    pass
            @bot.callback_query_handler(func=lambda call: True)
            def callback_inline(call):
                with open('mathbotbd.json', 'r') as file:
                    data = json.load(file)
                idtg = str(call.from_user.id)
                if call.data == "gm": 
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Алгебра')
                    btn2 = types.KeyboardButton('Геометрия')
                    btn3 = types.KeyboardButton('Информация')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(chat_id=call.from_user.id, text=f'''
                <i><b>Информация📜</b></i>

        <b><i>Статистика бота:</i></b>
        🙍‍♂<b>Пользуются сервисом: {len(data)}</b>
        
        <i>Выберите тип👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                elif call.data == "kalkulatora":
                    markup = types.InlineKeyboardMarkup(row_width = 2)


            bot.polling(none_stop=True)
        else:
            pass
main()