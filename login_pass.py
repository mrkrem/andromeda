def sign_up():
    login = input('Придумайте логин: ')
    password1 = input('Придумайте пароль: ')
    password2 = input('Введите пароль еще раз: ')
    if password1 == password2:
        write_to_file('logins.txt', login+'\n')
        write_to_file('passwords.txt', password1+'\n')
        print(f'Пользователь {login} успешно зарегистрирован')
    else:
        print('Пароли не схожи. Проверьте-ка еще раз')
        
def sign_in():
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    login_list = read_list('logins.txt')
    password_list = read_list('passwords.txt')
    if login in login_list: # если логин в списке логинов
        login_str = login_list.index(login) # находим его индекс
        true_password = password_list[login_str] # берем пароль  с таким же индексом
        if password == true_password:
            print('Вы успешно вошли в систему')
            return True
        else:
            print('Пароль неправильнй')
            return False
    else:
        print('Пользователя с таким логином не существует')
        return False
    
    
def write_to_file(filename, text):
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        
        
def read_list(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        text = file.read().split('\n')
        return text
        
acces = False
while True:
    if not access:
        print('Это программа БоберКор, и вот что она умеет: ')
        print('1 - зарегистрироваться')
        print('2 - войти в систему')
        print('3 - выйти из программы')
        action = input('Введите номер действия: ')
        if action == '1':
            sign_up()
        elif action == '2':
            acces = sign_in()
        elif action == '3':
            print('Спасибо за использование программы')
            break
    elif access:
        print('Вы в системе. Ураааааааааа')
    input('Нажмите Enter, чтобы продолжить')
        