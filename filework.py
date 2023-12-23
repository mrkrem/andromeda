# file = open('text.txt', mode='w',encoding='UTF-8')
# file.write('Скоро новый год придет,\n')
# file.write('Счастья крылышек полет')
# file.close()

# file = open('text.txt', mode='w',encoding='UTF-8')
# file.write('Время побыть с семьей')
# file.close()

# with open('text.txt', mode='a',encoding='UTF-8') as file:
#     file.write('\nОтдохни от дел')
import random
def file_write500():    
    with open('text.txt', mode='w',encoding='UTF-8') as file:
        for i in range(1, 501):
            file.write('Я буду заниматься программированием и вне занятий Андромеды\n')
    
    
def get_one_word(filename):    
    with open(filename, mode='r',encoding='UTF-8') as file:
        text = file.read().split('\n')
        return random.choice(text)
    
    
pril = get_one_word('prils.txt')
name = get_one_word('animals.txt')
print(f'В племени индейцев Тумба-Юмба вас бы звали {pril} {name}')
    
    
    
    
    

        
        
    