import json
def menu_uchenik(idtg): 
    with open('uchenik.json', 'r') as file:
        data = json.load(file)
    return  f'''
<i><b>Информация📜</b></i>

<b>ФИО: {data[idtg]["fio"]}</b>🙍‍♂
<b>Ваше расписание:</b>

<b>{1212}</b>


<i>Нажмите на кнопку👇🏻</i>
                    '''
def uchenik_kavnt(idtg):
    with open('uchenik.json', 'r') as file:
        data = json.load(file)
    with open('kvantorium.json', 'r') as file:
        kvan = json.load(file)
    f'''
                    <i><b>Информация📜</b></i>

        <b>Название: {message.text}</b>📰


<b>Расписание:</b>

<b>{r}</b>
                
<b>Кабинет - {k}</b>

<i>Связь с учителем - @{name}</i>

                <i>Выберите кнопку👇🏻</i>
                            '''
def kvant(mes, idtg):
    with open('uchitel.json', 'r') as file:
        data = json.load(file)
    with open('kvantorium.json', 'r') as file:
        kvan = json.load(file)
    return f'''
<i><b>Информация📜</b></i>

<b>Название: {mes}</b>📰
        
<b>Количество учеников: {len(kvan[mes]["ludi"])}</b>🙍‍♂️

<b>Описание квантума: {kvan[mes]["dop"]["bio"]["text"]}</b>
<i>Выберите кнопку👇🏻</i>
                    '''
def menu_uchitel(idtg):
    with open('uchitel.json', 'r') as file:
        data = json.load(file)
    return f'''
                <i><b>Информация📜</b></i>

        <b>ФИО: {data[idtg]["fio"]}</b>🙍‍♂
        
        <i>Нажмите на кнопку👇🏻</i>
                    '''

uchitel_kvant = f'''
        <i><b>Квантумы👩‍🏫</b></i>
<b>Ваши квантумы:</b>
                    '''
    
dopkvant = f'''
<i><b>Создать квантум👩‍🏫</b></i>

<b>Напишите название нового квантума:</b>
                    '''


uchenik_moikvant = f'''
<i><b>Мои квантумы👩‍🏫</b></i>

<b>Ваши квантумы:</b>
                    '''
                

ras = f'''
<i><b>Расписание📅</b></i>

<i>*Нажмите на день чтобы изменить или добавить</i>
'''

dop_day = f'''
<i><b>Добавить день➕</b></i>

<b>Какой день вы хотите добавить?</b>
'''




