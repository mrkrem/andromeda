import random
inventory = []
steps = 0


def gaw():
    print('Гав-гав-гав!')
    
def robot_forward():
    global steps
    steps+=1
    print('Робот идет вперед')
    
    
def robot_backward():
    print('Робот идет назад')
    global steps
    steps+=1
    
def robot_right():
    print('Робот идет вправо')
    global steps
    steps+=1

def robot_left():
    print('Робот идет влево')
    global steps
    steps+=1
    
def robot_scan():
    items = ['Ветка','Бутылка','Железо','Дерево','Алмаз','Золото']
    item = random.choice(items)
    print(f'Робот нашел предмет {item}')
    return item

def say_steps():
    print(f'Вы прошли {steps} шагов')
    
    
def robot_pickup(item):
    global inventory
    inventory.append(item)
    
def check_inventory():
    for index, item in enumerate(inventory,start=1):
        print(f'{index}.{item}')
        
def craft():
    recept1 = ['золото','золото','золото'] # золотой слиток
    recept2 = ['Золотой слиток','дерево'] # золотой меч
    recept3 = ['алмаз','алмаз','дерево'] # алмазный меч
    recepts = [recept1,recept2,recept3]
    recept_names = ['Золотой слиток','золотой меч','алмазный меч']
    print('Достпуны следущие рецепты: ')
    for index, recept in enumerate(recept_names, start=1):
        print(f'{index}.{recept}')
    choice = input('Выбери, что хочешь крафтить: ')
    if not choice.isdigit():
        print('Вводить можно только числа')
        return None # выход из функции
    choice = int(choice) - 1 # получаем нужный индекcc
    if choice not in range(0, len(recept_names)): # если выбрали не в диапазоне
        print('Рецепта с таким номером нет')
        return None
    choice_recept = recept_names[choice]
    print(f'Вы выбрали крафтить {choice_recept}')
    ingredients = recepts[choice]
    print(f'Ингредиенты: {ingredients}')
    for item in inventory:
        if item in ingredients:
            print(f'Уничтожен {item}')
            inventory.remove(item)
            ingredients.remove(item)
    if not ingredients:
        inventory.append(choice_recept)
        print(f'В инвентарь добавлен {choice_recept}')
    else:
        print('Не хватает ингредиентов')
    
    
    

    
def main():    
    while True:
        key = input('Введите клавишу(WASD, fec, x-выход): ')
        if key == 'w':
            robot_forward()
        if key == 'x':
            break
        elif key == 's':
            robot_backward()
        elif key == 'd':
            robot_right()
        elif key == 'a':
            robot_left()
        elif key == 'f':
            item = robot_scan()
            robot_pickup(item)
        elif key == 'e':
            check_inventory()
        elif key == 'h':
            say_steps()
        elif key == 'c':
            craft()
            
            


    


