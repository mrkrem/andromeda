import random

class Fighter:
    def __init__(self, name:str, name_fatality:str):
        self.name = name
        self.power = random.randint(1, 5)
        self.hp = 100
        self.nam_fat = name_fatality


fighter1 = Fighter('Скорпион', 'Скорпионья супер атака')
fighter2 = Fighter('Охлодулькин', 'Сосульки-Ударюльки')
fighter3 = Fighter('Кунг-фу панда', 'Скидыщ')
fighter4 = Fighter('Учитель математики', 'Удар в виде подфакториального субфакториала 30 в синусе 5 ')
fighter5 = Fighter('Учитель физики', 'Удар переменным током')
fighter6 = Fighter('Учитель русского языка и литературы', 'Деепричастный оборот')
fighter7 = Fighter('Учитель ИЗО', 'Удар циркулем за неправильное построение тригонометрии')
fighter8 = Fighter('Учитель истории', 'Удар бояром с ножом')
fighter9 = Fighter('Учитель английского языка', 'LONDON OF THE CAPITELE OF GRATE BTITAN')

fighters = [fighter1, fighter2, fighter3, fighter4, fighter5, fighter6, fighter7, fighter8, fighter9]
enemy1 = random.choice(fighters)
fighters.remove(enemy1)
enemy2 = random.choice(fighters)
fighters.append(enemy1)


print(f'{enemy1.name} VS {enemy2.name}')
