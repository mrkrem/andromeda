# class Phone:
#     def __init__(self,name:str, processor:str, camera:int, memory:int):
#         self.name = name
#         self.processor = processor
#         self.camera = camera
#         self.memory = memory
        
#     def make_photo(self):
#         print(f'{self.name} делает фото')
        
#     def typing_sms(self):
#         print(f'{self.name} печатает сообщение...')
#     def game_processing(self):
#         print(f'{self.name} играет в игру...')
            
# phone1 = Phone('Sony','Snapdragon', 50, 512)
# phone2 = Phone('Iphone', 'M1', 12, 64)
# print(phone1.name)
# print(phone2.name)
# phone1.make_photo()
# phone1.typing_sms()
# phone1.game_processing()



class Human():
    def __init__(self, name,surname,age,weight,growth):
        self.name = name
        self.surname = surname
        self.age = age
        self.weight = weight
        self.growth = growth
    def happy_birthday(self):
        self.age += 1
        print(f'{self.name},поздравляю тебя с днем рождения!!! ТЕбе исполнилось {self.age} лет')

human = Human('Вася', 'Пупкин',4,5,30)
human.happy_birthday()



class PhrasweDecoration:
    def decorate(self, phrase):
        line = '-' * (len(phrase)+4)
        print(line)
        print('|', phrase, '|')
        print(line)
        
        
text = PhrasweDecoration()
text.decorate('Я люблю ООП')


class Father:
    def __init__(self, name:str, age:int):
        self.name = name.capitalize()
        self.age = age
        self.gender = 'мужчина'
        self.power = 0
        
    def swim(self):
        print(f'{self.name} плавает брассом')
        
    def dispute(self):
        print(f'{self.name} спорит басом')
        
    def chopping(self):
        self.power += 1
        print(f'{self.name} рубит дрова. Сила папы = {self.power}')
        
father = Father(name='Олег', age=55)
father.swim()
father.dispute()
father.chopping()
 
class Son(Father):
    def __init__(self, name: str, age: int, sport:int):
        super().__init__(name, age)
        self.sport = sport    
    
    def dispute(self):
        super().dispute()
        print(f'{self.name} спорит')
        

son = Son('Роман', 5, 23)
son.swim()
son.dispute()
son.chopping()
        
        