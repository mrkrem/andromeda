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