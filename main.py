import os
import time

banner = """

╔═╗    ╔═╗   ╔══╦═╦═╦╗ 
║╔╬╦╦═╗╠═╠╦╗ ╚╗╔╣║║║║║
║╚╣╔╣╬╚╣═╣║║  ║║║║║║║╚╗
╚═╩╝╚══╩═╬╗║  ╚╝╚═╩═╩═╝
         ╚═╝

┌─────────────────────────────────────────┐
│Разработчик: @Fr31zep ТГК: @crazytoolsoft│
│─────────────────────────────────────────│
│                  FREE                   │
└─────────────────────────────────────────┘
┌───────────────────────────────┬─────────┐
│[1] Поиск по номеру            │   V.4   │
│[2] Поиск по IP                └─────────│
│[3] Поиск по нику                        │ 
│[4] DDDOS                                │
│[5] Мануал по доксу                      │
│[6] Мануал по свату                      │
│[7] Мануал по сносу ТГ                   │
│[8] Генератор личности                   │
│[9] Генератор карты                      │
│[10] Поиск по базе данных                │
│[11] Св@т б@нв0рD                        │
│[12] Бомбер ТГ                           │
│[13] Информация                          │
│[14] Выйти                               │
└─────────────────────────────────────────┘

"""
print(banner)
choice = input("Введите номер желаемой функции -> ")
if choice == "1":
    os.system("clear")
    os.system("python phone.py")
elif choice == "2":
    os.system("clear")
    os.system("python ip.py")
elif choice == "3":
    os.system("clear")
    os.system("python nick.py")
elif choice == "4":
    os.system("clear")
    os.system("python ddos.py")
elif choice == "5":
    os.system("clear")
    os.system("python doks.py")
elif choice == "6":
    os.system("clear")
    os.system("python swat.py")
elif choice == "7":
    os.system("clear")
    os.system("python snos.py")
elif choice == "8":
    os.system("clear")
    os.system("python generate.py")
elif choice == "9":
    os.system("clear")
    os.system("python card.py")
elif choice == "10":
    os.system("clear")
    os.system("python searchb.py")
elif choice == "11":
    os.system("clear")
    os.system("python antispam.py")
elif choice == "12":
    os.system("clear")
    os.system("python snostg.py")
elif choice == "13":
    os.system("clear")
    os.system("python info.py")
elif choice == "14":
    os.system("clear")
    os.system("python quit.py")
else:
    print("[?] Прозошла ошибка, проверьте вводимые данные! ")
    time.sleep(3)
    os.system("clear")
    os.system("python main.py")
