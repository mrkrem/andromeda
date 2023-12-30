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
    
def write_to_file(filename, text):
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
        
        
        
         
while True:
    print('Это программа БоберКор, и вот что она умеет: ')
    print('1 - зарегистрироваться')
    print('2 - выйти из программы')
    action = input('Введите номер действия: ')
    if action == '1':
        sign_up()
    if action == '2':
        print('Спасибо за использование программы')
        break
    input('Нажмите Enter, чтобы продолжить')