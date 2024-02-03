from cost import *
import random

def pay():
    money = random.choice(['да','нет'])
    if money == 'да':
        print('Вы оплатили ваш заказ')
    else:
        print('Вам не хватило денег')