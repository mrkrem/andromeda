import random
inventory = []
def gaw():
    print('Гав-гав-гав!')
    
def robot_forward():
    print('Робот идет вперед')
    
    
def robot_backward():
    print('Робот идет назад')
    
def robot_right():
    print('Робот идет вправо')

def robot_left():
    print('Робот идет влево')
    
def robot_scan():
    items = ['Ветка','Бутылка','Железо','Дерево']
    item = random.choice(items)
    print(f'Робот нашел предмет {item}')
    return item

    
    
def robot_pickup(item):
    global inventory
    inventory.append(item)
    
    
    
    

    
    
while True:
    key = input('Введите клавишу: ')
    if key == 'w':
        robot_forward()
    elif key == 's':
        robot_backward()
    elif key == 'd':
        robot_right()
    elif key == 'a':
        robot_left()
    elif key == 'f':
        item = robot_scan()
        robot_pickup(item)
        print(inventory)
        
        


    


