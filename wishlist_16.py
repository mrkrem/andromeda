print('Это приложение Список Желаний')
name = input('Как к вам можно обращаться: ')
wishlist = []

while True:
    print(f'Меню:')
    print('1 - добавить желание')
    print('2 - показать все желания')
    print('3 - удалить желание')
    action = input(F'Что хотите сделать, {name} -> ')
    if action == '1':
        wish = input(f'{name}, какое желание хотите добавить: ')
        if wish not in wishlist:
            wishlist.append(wish)
            
    elif action == '2':
        for i in range(1,len(wishlist)+1):
            print(i)
        for wish in wishlist:
            print(wish)
    elif action == '3':
        for i, wish in enumerate(wishlist, start = 1):
            print(f'{i}. {wish}')
        delete_index = input(f'{name}, введите номер желания для удаления: ')
        delete_index = int(delete_index)
        delete_index = int(delete_index) - 1
        delete_wish = wishlist.pop(delete_index)
        print(f'Вы исполнели желание {delete_index}' )
        
        
        
        
        
        
    input('Нажмите Enter, чтобы продолжить')

    
    
    
    
        
            
        