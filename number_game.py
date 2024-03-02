import random
print("Это игра 'Угадай число'")
print(" Я загадаю тебе число от 1 до 100,а ты попробуешь угадать это число =]")
nameuser = input("Введите свое имя: ")
money = 0
iq = 0
print(f"Приятно познакомиться, {nameuser}")
print(f"Твой баланс: {money} монет,выиграй игру чтобы получить 5 монет")
game_round = 0
while game_round < 3:
    game_round+=1
    print(F"Раунд {game_round}")
    attempts = 1
    number_comp = random.randint(1, 100)
    while attempts < 10:
        user_number = input(f"Введите число,{nameuser}: ")
        if not user_number.isdigit():
            print(f"{nameuser},вы ввели не число")
            continue
        attempts += 1
        user_number = int(user_number)

        user_number = int(user_number)
        print(f"Вы ввели {user_number}")
        if user_number > number_comp:
            print(f"Вы ввели больше, чем у меня,{nameuser}")
        elif user_number < number_comp:
            print(f"Вы вели меньше, чем у меня,{nameuser}")
        elif user_number == number_comp:
            print(f"Вы угадали! Вы безупречны,{nameuser}")
            money += 5
            print(f"У вас сейчас {money} монет")
            break
            if attempts == 10:
                print("Все попытки истрачены, вы не угадали")




print(f"Вы прошли легкий уровень,{nameuser}.Теперь вам доступен магазин!")
shop = input(
    "Вы автоматически вошли в магазин,приеобретите IQ прописав в строку команду /buy: "
)
if shop == "/buy":
    money -= 1
    print(f"С баланса снята 1 монетка,ваш баланс {money}")
    iq += 1
print(
    "Чем больше IQ тем ты становишься более умным в игре")