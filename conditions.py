exp = 2 + 2 == 5
print(exp)

age = 13
if age == 13:
    print("Тебе 13") 
if age >  11:
    print("Тебе больше 11")
if age < 14:
    print("Тебе меньше 14")
if age >= 13:
    print("Тебе больше 13 или тебе 13")
if age <= 13:
    print("Тебе меньше 13 или тебе 13")
if age != 13:
    print("Мне не 13")


temp = int(input("Введите температуру: "))
if temp < 0:
    print("Холодно")
elif temp < 10:
    print("Прохладно")
elif temp < 25:
    print('Тепло')
elif temp < 35:
    print("Жарко")
else:
    print("Оооочень жарко")
number = int(input("Введите число: "))
if number %2 == 1:
     print("Число нечетное")
else:
    print("Число четное")
