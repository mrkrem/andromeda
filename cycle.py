# counter = 1
# while counter <= 10:
#     print(counter)
#     counter += 1

# sandwich = 1
# while sandwich <= 30:
#     print(sandwich)
#     sandwich += 1
#     print(f"Сделал {sandwich}-й бутерброд")
#     sandwich+=1
student = 1
while student <= 6:
    print(student)
    print(f"Сосчитал {student}-ого ученика")
    student += 1
import time
number = 10
summa = 0
while number > 0:
    summa += number
    time.sleep(1)
    print(f"Прибавили {number}, получилось {summa}")
    number -= 1
number = 10
plusn = 5
while number <= 20:
    number += plusn
    print(f"Прибавили {number}, получилось {plusn}")
    
rain = True
while rain:
    print("Я пью чай")
    stop = input("Дождь кончился? (да/нет)")
    if stop == "да":
        print("Дождь кончился")
        break
    
    