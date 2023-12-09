def plus():
    a = x + y
    print(f'Ответ: {a}')
def minus():
    a = x - y
    print(f'Ответ: {a} ')
def delenie():
    a = x / y
    print(f'Ответ: {a}')
def umn():
    a = x * y
    print(f'Ответ: {a}')
def input_number(input_pharse):
    x = input(input_pharse)
    if not x.isdigit():
        print('Вводить можно только числа')
        return input_number(input_pharse)
    return int(x)
    
while True:
    x = input_number('Введите первое число: \n')

    
    y = input_number('Введите второе число: \n')
    print('Меню: ')
    print('1 - +')
    print('2 - -')
    print('3 - /')
    print('4 - *')
    action = input('Введите  знак операции: \n ')
    if action == '+':
        plus()
    elif action == '-':
        minus()
    elif action == '/':
        delenie()
    elif action == '*':
        umn()
        