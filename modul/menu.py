from constatnts import *
from order import *


def choice_pizza():
    print('Добро пожаловать в пиццерию "PIZZA DREAM"!')
    print('Меню пиццерии:')
    for i, pizza in enumerate(PIZZA):
        print(f'{i}.{pizza} - {COST[i]} рублей')
    while True:
        order = int(input('Выберите свою пиццу >>>')) - 1
        get_order(order_pizza=order)
        print('Пицца добавлена в корзину!')
        flag = input('Хотите продолжить заказывать? ')
        if flag.upper() == 'НЕТ':
            print('Вы вышли из меню')
            break
        
