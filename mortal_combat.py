import random

class Fighter:
    def __init__(self, name:str, name_fatality:str):
        self.name = name
        self.power = random.randint(1, 5)
        self.hp = 100
        self.nam_fat = name_fatality
        self.fat_switch = True
        
    def attack(self, attacked_fighter):
        if self.fat_switch:
            self.fatality(attacked_fighter)
        attacked_fighter.hp -= self.power
        print(f'{self.name} наносит {self.power} ед. урона персонажу {attacked_fighter.name}')
        self.harakiri()
        
            
    def say_info(self):
        print(f'У персонажа {self.name} {self.hp} ед здоровья, {self.power} единиц силы')
        
    def fatality(self, attacked_fighter):
        if self.hp < 15:
            damage = random.randint(0, attacked_fighter.hp)
            attacked_fighter.hp -= damage
            print(f'{self.name} принимает суператаку {self.nam_fat} {self.name} и наносит {damage} ед. урона персонажу {attacked_fighter.name}')
            self.fat_switch = False
            
            
    def harakiri(self):
        if self.hp < 5 and random.randint(1, 2)==1:
            print(f'{self.name} совершил харакири')
            self.hp = 0
            


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

while True:
    enemy1.attack(enemy2)
    enemy2.attack(enemy1)
    enemy1.say_info()
    enemy2.say_info()
    if enemy1.hp <= 0 and enemy2.hp <= 0:
        print('Ничья')
        break
    elif enemy2.hp <= 0:
        print(f'{enemy1.name} победил')
        break