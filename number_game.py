import random
money = 0
print("Это игра 'Угадай число'")
print(" Я загадаю тебе число от 1 до 100,а ты попробуешь угадать это число =]")
nameuser = input("Введите свое имя: ")
print(f"Приятно познакомиться, {nameuser}")
print(f"Твой баланс: {money} монет,выиграй игру чтобы получить 5 монет")
attempts = 8
number_comp = random.randint(1, 100)
while attempts > 0:
    user_number = input("Введите число: ")
    user_number = int(user_number)
    print(f'Вы ввели {user_number}')
    if user_number > number_comp:
        print("Вы ввели больше, чем у меня")
    elif user_number < number_comp:
        print("Вы вели меньше, чем у меня")
    elif user_number == number_comp:
        print(f"Вы угадали! Вы безупречны,{nameuser}!")
        money +=5
        print(F"Твой баланс: {money}")



    