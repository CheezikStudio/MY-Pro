import telebot 
import json
from telebot import types
import random
import time
def main():
    while True:
        try:
            bot = telebot.TeleBot('6290633013:AAHcICJniGQJwOGICxpwilTO3U0EYcHbnSs')
            @bot.message_handler(commands=["start"])
            def start(message, res=False):
                with open('data.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if idtg in data:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Добавить ID')
                    btn2 = types.KeyboardButton('Помощь')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
        <i><b>Профиль🙍‍♂</b></i>

    <b>Подписка: {data[idtg]["sub"]}</b>🙍‍♂

    <b>ID: {data[idtg]["ID"]}</b>🙍‍♂

    <i>Нажми на кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    
                    bot.register_next_step_handler(message, menu)
                
                elif idtg == "1058097307" or idtg == "1359842271":
                    text = ""
                    for i in data:
                        text += f'''{i} - <code>{data[i]["ID"]}</code> \n'''
                    markup = types.InlineKeyboardMarkup(row_width = 1)
                    btn1 = types.InlineKeyboardButton(text="Новая ссылка", callback_data='new')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f'''
                    Главное меню:
            Софт купили - {len(data)}
            {text}
                    ''',  reply_markup=markup, parse_mode='HTML')
                    
                else:
                    if " " in message.text:
                        try:
                            with open('s.json', 'r') as file:
                                bd = json.load(file)
                            if message.text.split(" ")[1] in bd and time.time() - bd[message.text.split(" ")[1]] <= 60:
                                bot.send_message(message.chat.id, f"<b>Поздровляем вы купили наш софт lnvareTap!</b>", parse_mode='HTML')
                                with open('data.json', 'r') as file:
                                    data = json.load(file)
                                idtg = str(message.from_user.id)
                                
                                rbr = {"sub": "✅", "ID": "Не заполнено"}
                                data[idtg] = rbr
                                with open('data.json', 'w') as file:
                                    json.dump(data, file, indent=4)
                                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                                btn1 = types.KeyboardButton('Добавить ID')
                                btn2 = types.KeyboardButton('Помощь')
                                markup.add(btn1, btn2)
                                bot.send_message(message.chat.id, f'''
                    <i><b>Профиль🙍‍♂</b></i>

                <b>Подписка: {data[idtg]["sub"]}</b>🙍‍♂

                <b>ID: {data[idtg]["ID"]}</b>🙍‍♂

                <i>Нажми на кнопку👇🏻</i>
                                ''',  reply_markup=markup, parse_mode='HTML')
                                
                                bot.register_next_step_handler(message, menu)
                        except:
                            bot.send_message(message.chat.id, f"<b>Вы не купили наш софт lnvareTap!❌</b>", parse_mode='HTML')
            def menu(message):
                with open('data.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == "Добавить ID":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Назад')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f"<i>Скиньте ссылку на ваш ID устройства:</i>", parse_mode='HTML',  reply_markup=markup)
                    bot.register_next_step_handler(message, ID)
                elif message.text == "Помощь":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
                    btn1 = types.KeyboardButton('Назад')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f"<i>Нема</i>",  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu)
                else:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Добавить ID')
                    btn2 = types.KeyboardButton('Помощь')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
        <i><b>Профиль🙍‍♂</b></i>

    <b>Подписка: {data[idtg]["sub"]}</b>🙍‍♂

    <b>ID: {data[idtg]["ID"]}</b>🙍‍♂

    <i>Нажми на кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu)
            def ID(message):
                with open('data.json', 'r') as file:
                    data = json.load(file)
                idtg = str(message.from_user.id)
                if message.text == "Назад":
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 3)
                    btn1 = types.KeyboardButton('Добавить ID')
                    btn2 = types.KeyboardButton('Помощь')
                    markup.add(btn1, btn2)
                    bot.send_message(message.chat.id, f'''
        <i><b>Профиль🙍‍♂</b></i>

    <b>Подписка: {data[idtg]["sub"]}</b>🙍‍♂

    <b>ID: {data[idtg]["ID"]}</b>🙍‍♂

    <i>Нажми на кнопку👇🏻</i>
                    ''',  reply_markup=markup, parse_mode='HTML')
                    bot.register_next_step_handler(message, menu)
                else:
                    with open('data.json', 'r') as file:
                        data = json.load(file)
                    idtg = str(message.from_user.id)
                    link = message.text
                    rbr = {"sub": "✅", "ID": link}
                    data[idtg] = rbr
                    with open('data.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
                    btn1 = types.KeyboardButton('В Меню')
                    markup.add(btn1)
                    bot.send_message(message.chat.id, f"ID Указано!✅", parse_mode='HTML',  reply_markup=markup)
                    bot.send_message(1359842271, f"{link} - Новая ссылка")
                    bot.register_next_step_handler(message, menu)

            @bot.callback_query_handler(func=lambda call: True)
            def call_menu(call):
                if call.data == "new":
                    
                    i = random.randint(1, 100000)
                    t = time.time()
                    with open('s.json', 'r') as file:
                        bd = json.load(file)
                    bd[str(i)] = t
                    with open('s.json', 'w') as file:
                        json.dump(bd, file, indent=4)
                    bot.send_message(chat_id=call.from_user.id, text = f'''
Ссылка - <code>http://t.me/UnveriteTap_bot?start={i}</code>
Действует ровно 1 минуту!
                    ''', parse_mode='HTML')
                
            bot.polling(none_stop=True)
        
        except:
            pass

main()