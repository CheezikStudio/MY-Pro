# 5790837052:AAG18gKhILjoR88qXrFva_9LTBCG9cDR2ko
import telebot 
import time
import json
from telebot import types
import random
def main():
    while True:
        if True:
            bot = telebot.TeleBot('5790837052:AAG18gKhILjoR88qXrFva_9LTBCG9cDR2ko')
            @bot.message_handler(commands=["start"])
            def start(message, res=False):
                print(message)
                with open('shooll.json', 'r') as file:
                    data = json.load(file)
                with open('bd_shooll.json', 'r') as file:
                    bd = json.load(file)
                idtg = str(message.from_user.id)
                if idtg not in data:
                    with open('shooll.json', 'r') as file:
                        data = json.load(file)
                    name = str(message.chat.first_name)
                    idtg = str(message.from_user.id)
                    
                    rbr = {"fio": "❌", "class" : "❌", "dop1": [], "dop2": {}, "dop3": ""}
                    data[idtg] = rbr
                    with open('shooll.json', 'w') as file:
                        json.dump(data, file, indent=4)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                btn1 = types.KeyboardButton('Конкурсы🥇')
                btn2 = types.KeyboardButton('Мероприятия🗓')
                btn3 = types.KeyboardButton('Профиль🙍‍♂')
                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id, f'''
            <i><b>Информация📜</b></i>

    <b>ФИО: {data[idtg]["fio"]}</b>🙍‍♂

    <b>Класс: {data[idtg]["class"]}</b>👩‍🏫

    <b>Рубли: <i>В разработке...💰</i></b>

    <i>Нажми на кнопку👇🏻</i>
                ''',  reply_markup=markup, parse_mode='HTML')
                
                bot.register_next_step_handler(message, menu)
            def menu(message):
                with open('shooll.json', 'r') as file:
                    data = json.load(file)
                with open('bd_shooll.json', 'r') as file:
                    bd = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Конкурсы🥇':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Спортивные⚽')
                    btn2 = types.KeyboardButton('Творческие🎨')
                    btn3 = types.KeyboardButton('Задания от учителя👩‍🏫')
                    btn4 = types.KeyboardButton('Итоги🏆')
                    btn5 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3, btn4, btn5)
                    bot.send_message(message.chat.id, f'''
        <i><b>Конкурсы🥇</b></i>
            
<b>Здесь собраны самые крутые конкурсы которые проводит наша школа и участники школьного правительства!</b>
            
<i>Выбери категорию которая тебе подходит👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, contest)
                elif message.text == 'Мероприятия🗓':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Тест')
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
        <i><b>Мероприятия🗓</b></i>
            
        
<b>В этом разделе ты можешь посмотреть интересные мероприятия которые будут проходить в нашей школе!</b>
            
            
<i>Выбери на какое мероприятие хочешь попасть👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, merop)
                elif message.text == 'Профиль🙍‍♂':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Изменить класс👩‍🏫')
                    btn2 = types.KeyboardButton('Изменить ФИО🙍‍♂')
                    btn3 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
         <i><b>Профиль🙍‍♂</b></i>

    <b>ФИО: {data[idtg]["fio"]}</b>🙍‍♂

    <b>Класс: {data[idtg]["class"]}</b>👩‍🏫

    <b>Рубли: <i>В разработке...💰</i></b>

    <i>Нажми на кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, prof)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Я тебя не понял(( Возвращайся обратно! 
                    ''',  reply_markup=markup, parse_mode='HTML')





            def prof(message):
                with open('shooll.json', 'r') as file:
                    data = json.load(file)
                with open('bd_shooll.json', 'r') as file:
                    bd = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Конкурсы🥇')
                    btn2 = types.KeyboardButton('Мероприятия🗓')
                    btn3 = types.KeyboardButton('Профиль🙍‍♂')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                <i><b>Информация📜</b></i>

        <b>ФИО: {data[idtg]["fio"]}</b>🙍‍♂

        <b>Класс: {data[idtg]["class"]}</b>👩‍🏫

        <b>Рубли: <i>В разработке...💰</i></b>

        <i>Нажми на кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu)
                elif message.text == 'Изменить класс👩‍🏫':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    <b>Напишите свой новый класс:</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, klacc)
                elif message.text == 'Изменить ФИО🙍‍♂':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    <b>Напишите ФИО:</b>
                    <i>*Отчество не обязательно</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, fio)
                elif message.text == 'Вывести рубли💰':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    <b>Функция временно недоступна!</b>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, prof_back)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Я тебя не понял(( Возвращайся обратно! 
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, prof_back)
            def klacc(message):
                pass
            def merop(message):
                with open('shooll.json', 'r') as file:
                    data = json.load(file)
                with open('bd_shooll.json', 'r') as file:
                    bd = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Конкурсы🥇')
                    btn2 = types.KeyboardButton('Мероприятия🗓')
                    btn3 = types.KeyboardButton('Профиль🙍‍♂')
                    markup.add(btn1, btn2, btn3)
                    bot.send_message(message.chat.id, f'''
                <i><b>Информация📜</b></i>

        <b>ФИО: {data[idtg]["fio"]}</b>🙍‍♂

        <b>Класс: {data[idtg]["class"]}</b>👩‍🏫

        <b>Рубли: <i>В разработке...💰</i></b>

        <i>Нажми на кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu)
                if message.text == 'Тест':
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Записаться✅')
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2)
                    file = open("text.jpg", "rb")
                    bot.send_photo(message.chat.id, file, f'''
                <i><b>Тест</b></i>
            
            <b>Описание</b>

            <b>Записатись: {bd["meriop"]["test1"]["test"]}</b>

            <i>Хочешь записаться?</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    key = "test1"
                    kol = "test"
                    kol_bd = "test_bd"
                    bot.register_next_step_handler(message, zap, kol, key, kol_bd)

            def zap(message, kol, key, kol_bd):
                with open('shooll.json', 'r') as file:
                    data = json.load(file)
                with open('bd_shooll.json', 'r') as file:
                    bd = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == 'Назад👈🏻':
                    reply_markup = types.ReplyKeyboardRemove()
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Тест')
                    btn2 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
        <i><b>Мероприятия🗓</b></i>
            
        
<b>В этом разделе ты можешь посмотреть интересные мероприятия которые будут проходить в нашей школе!</b>
            
            
<i>Выбери на какое мероприятие хочешь попасть👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, merop)
                elif message.text == 'Записаться✅':
                    if data[idtg]["fio"] == "\u274c":
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                        <b>Пожалуйста укажите своё ФИО в <i>Профиле</i> для участия в мероприятиях!)</b>
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, start)
                    elif data[idtg]["fio"] not in bd["meriop"][key][kol_bd]:
                        pol = bd["meriop"][key][kol] + 1
                        pol1 = bd["meriop"][key][kol_bd].append("j")
                        print(pol1)
                        bd["meriop"][key][kol] = pol
                        bd["meriop"][key][kol_bd] = pol1
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                        <b>Ждём тебя на мероприятии!)</b>
                        ''',  reply_markup=markup, parse_mode='HTML')
                        with open('bd_shooll.json', 'w') as file:
                            json.dump(bd, file, indent=4)
                        bot.register_next_step_handler(message, start)
                    elif data[idtg]["fio"] in bd["meriop"][key][kol_bd]:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                        <b>Вы уже зарегистрированы на мероприятии!</b>
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, merop_back)
                    else:
                        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                        btn1 = types.KeyboardButton('Назад👈🏻')
                        markup.add(btn1)
                        bot.send_message(message.chat.id, f'''
                        Я тебя не понял(( Возвращайся обратно! 
                        ''',  reply_markup=markup, parse_mode='HTML')
                        bot.register_next_step_handler(message, merop_back)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('Назад👈🏻')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Я тебя не понял(( Возвращайся обратно! 
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, merop_back)
            def merop_back(message):
                with open('shooll.json', 'r') as file:
                    data = json.load(file)
                with open('bd_shooll.json', 'r') as file:
                    bd = json.load(file)
                idtg = str(message.from_user.id)
                reply_markup = types.ReplyKeyboardRemove()
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                btn1 = types.KeyboardButton('Тест')
                btn2 = types.KeyboardButton('Назад👈🏻')
                markup.add(btn1, btn2)
                bot.send_message(message.chat.id, f'''
        <i><b>Мероприятия🗓</b></i>
        
    
<b>В этом разделе ты можешь посмотреть интересные мероприятия которые будут проходить в нашей школе!</b>
        
        
<i>Выбери на какое мероприятие хочешь попасть👇🏻</i>
                ''',  reply_markup=markup, parse_mode='HTML')
                bot.register_next_step_handler(message, merop)
            bot.polling(none_stop=False)
        else:
            pass
main()