
def main():
    import random
    import time
    # переменные
    udochka = 0
    braim_nps = 0
    money = 150
    lvl = 0
    # функции
    def TextTok():      
        print('TextTok приветствует вас!')
        print('Вы можете смотреть видео,а также снимать свои')
        print('Меню: ')
        print('1.Снимать видео')
        print('2.Смотреть видео')
        print('3. Выйти из приложения TextTok')
        while True:
            vop = input('Введите номер действия: ')
            if vop == '2':
                bot_video = random.choice(['Гейминг','Животные','Развлекательные'])
                print(f'Вам попалось видео на тему: {bot_video}')
                if bot_video == 'Гейминг':
                    tematika = random.choice(['Завтра начнётся закрытое бета-тестирование Escape from Tarkov Arena','В этом году мы не узнаем ничего нового о Sunautica 3','One Puch Man World выходит 30 января на PC и мобильных устройствах','Через неделю хоррор Choo-Choo Charle выйдет на консолях'])
                    print(tematika)
                if bot_video == 'Животные':
                    tematika = random.choice(['В Австралии найдены живыми ящерицы,которые считались вымершими','Шимпанзе,всю жизнь прожившую в клетке,выпустили в заповедник под открытым небом','В зоопарке Новосибирска впервые родился детёныш крошечной антилопы дик-дик',''])
                    print(tematika)
                if bot_video == 'Развлекательне':
                    tematika = random.choice(['Телефоны в 2002 - Я сделан из самого крепкого материала во вселенной.Меня можно заряжать раз в неделю.Телефоны 2023 - Не трогай меня,пожалуйста.А то я сломаюсь.Ты не заряжал меня уже 3 часа.Пока','Подростки в 1900х - Надеюсь,что выживу.Подростки сейчас - Надеюсь,кому нибудь понравится мое видео в TextTok'])
                    print(tematika)
            if vop == '1':
                tema_video = input('На какую тему хотите снять видео: ')
                print(f'Вы успешно засняли видео - {tema_video}')
            if vop == '3':
                print('Вы вышли из приложения TextTok')
                break
    def calc():
        print('Калькулятор')
        print('Чтобы выйти пользуйтесь клавишой E')
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
            print('5 - E - выход')
            action = input('Введите  знак операции: \n ')
            if action == '+':
                plus()
            elif action == '-':
                minus()
            elif action == '/':
                delenie()
            elif action == '*':
                umn()
            elif action == 'e':
                print('Вы вышли с калькулятора')
                break

    def cnb():
        print('Игра - Камень,ножницы,бумага')
        print('Чтобы выйти пользуйтесь клавишой E')
        while True:
            print('Выбор хода: ')
            print('1. Камень')
            print('2. Ножницы')
            print('3. Бумага')
            hod = input('Введите номер предмета которым хотите играть: ')
            if hod == '1':
                print('Вы выбрали Камень')
                hod_bot = random.choice(['Камень','Ножницы','Бумага'])
                print(f'Бот сходил предметом {hod_bot}')
                if hod == '1' and hod_bot == 'Камень':
                    print('Ничья')
                    time.sleep(5)
                if hod == '1' and hod_bot == 'Ножницы':
                    print('Вы победили!!!')
                    time.sleep(5)
                if hod == '1' and hod_bot == 'Бумага':
                    print('Вы проиграли(((')
                    time.sleep(5)
            if hod == '2':
                print('Вы выбрали предмет Ножницы')
                hod_bot = random.choice(['Камень','Ножницы','Бумага'])
                print(f'Бот сходил предметом {hod_bot}')
                if hod == '2' and hod_bot == 'Камень':
                    print('Вы проиграли(((')
                    time.sleep(5)
                if hod == '2' and hod_bot == 'Ножницы':
                    print('Ничья')
                    time.sleep(5)
                if hod == '2' and hod_bot == 'Бумага':
                    print('Вы победили!!!')
                    time.sleep(5)
            if hod == '3':
                print('Вы выбрали предмет Бумага')
                hod_bot = random.choice(['Камень','Ножницы','Бумага'])
                print(f'Бот сходил предметом {hod_bot}')
                if hod == '3' and hod_bot == 'Камень':
                    print('Вы выиграли!!!')
                    time.sleep(5)
                if hod == '3' and hod_bot == 'Ножницы':
                    print('Вы проиграли(((')
                    time.sleep(5)
                if hod == '3' and hod_bot == 'Бумага':
                    print('Ничья')
                    time.sleep(5)
                

            
                
                
                
            if hod == 'e':
                print('Вы вышли с игры - Камень,ножницы,бумага')
                break
    def zametki():
        print('Заметки')
        print('Чтобы выйти пользуйтесь клавишой E')
        while True:
            zam = input('Введите текст: ')
            print(f'Вы написали {zam}')
            if zam == 'e':
                print('Вы вышли из заметок')
                break      
                
    print('Наконец-то я прилетел в этот солнечный город Лос Анджелс')
    print('Подсказка: Чтобы ходить пользуйтесь W A S D,а чтобы выйти-x.Так же в игре доступны ограбления,но они доступны от 15 уровня.Обворовывайте людей чтобы поднять уровень и заработать деньги - пользуйтесь клавишой j.Чтобы ознакомиться со всеми функциями игры пользуйтесь клавишой i')
    # ходьба и управление
    while True:
        key = input('Управляйте: ')
        if key == 'x':
            break
        if key == 'w':
            print('Вы идёте вперед')
        if key == 's':
            print('Вы идёте назад')
        if key == 'a':
            print('Вы идёте налево')
        if key == 'd':
            print('Вы идёте направо')
        if key == 'j':
            print('Вы ограбили человека')
            money += 50
            lvl += 0.5
            print(f'Ваш баланс - {money}')
            print(f'Ваш игровой уровень - {lvl}')
        if key == 'i':
            print('Дополнительные функции игры для пользования телефоном: ')
            print('1. Чтобы посмотреть видео на платформе TextTok пользуйтесь клавишой T')
            print('2. Чтобы зайти в калькулятор в телефоне пользуйтесь клавишой C')
            print('3. Чтобы зайти в игру камень ножницы бумага в телефоне пользуйтесь клавишой B')
            print('4. Чтобы открыть заметки пользуйтесь клавишой V ')
            print('Дополнительные функции игры: ')
            print('1. Чтобы угнать автомобиль пользуйтесь клавишой E (большая)')
            
        
        if key == 't':
            TextTok()
            if lvl == 15:
                print('Вам доступны ограбления!Чтобы начать ограбление пользуйтесь клавишой K.И ещё хотим вам сказать,что если вы будете в ограблениях нажимать на лишние кнопки ограбление завершится ')

                
        if key == 'c':
            calc()
        if key == 'b':
            cnb()
        if key == 'v':
            zametki()
        if key == 'E':
            print('Вы угнали автомобиль.Для езды пользуйтесь клавишами W A S D.Чтобы выйти из автомобиля пользуйтесь клавишой E (большой)')
            while True:
                key = input('Управляйте автомобилем: ')
                if key == 'w':
                    print('Вы едете вперёд')
                if key == 's':
                    print('Вы едете назад')
                if key == 'a':
                    print('Вы едете налево')
                if key == 'd':
                    print('Вы едете направо')
                if key == 'E':
                    print('Вы вышли с автомобиля')
                    break
        if lvl >= 15:
            print('Вам доступны ограбления!Чтобы начать одно из ограблений пользуйтесь клавишой E  ')
        if key == 'k' and lvl >= 15:
            print('Доступные ограбления: ')
            print('1.Ограблние дома')
            print('2.Ограбление ювелирного магазина')
            print('3.Ограбление банка')
            key = input('Выберите ограбление написав номер ограбления: ')
            if key == '1':
                braim_nps += 1
                print('Вы начали задание - ограбление дома')
                time.sleep(5)
                print('Лео: Привет!!!Я так понимаю ты встал на темную сторону? ')
                time.sleep(5)
                print('Вы: Ззздраввв ствуйте?)Вы кто? ')
                time.sleep(5)
                print('Лео: Я Лео - организатор всяких черных делишек.Мой братан мне сказал что ты хочешь ограбить дом...Это так?Я могу тебе помочь в этом')
                time.sleep(5)
                print('Вы: Да,я хочу!!!')
                time.sleep(5)
                print('Лео: Тогда пошли за мной,будем делать план')
                time.sleep(5)
                print('Лео: Итак,ты хочешь ограбить дом...Впринципе ограбление не сложное,главное не делать лишних действий')
                time.sleep(5)
                print('Лео: Смотри,ты можешь даже сам ограбить дом,но для анонимности купи маску и перчатки.По поводу оружия,тебе оно в ограблении не понадобится')
                print('Вы купили маску и перчатки')
                print('Лео: Удачи в ограблении.Я буду говорить в наушник действия которые ты будешь выполнять,прошу не делай лишнего!')
                time.sleep(5)
                print('Вы: Так точно...')
                print('Лео: Иди вперед')
                print('Подсказка: Используйте клавишу W чтобы идти вперёд')
                key = input('Управляйте: ')
                if key == 'w':
                    print('Bы идёте вперед')
                    print('Лео: Правильно,видишь ту лестницу?Аккуратно поднимись по ней...')
                    print('Подсказка: Пользуйтесь клавишой H чтобы подняться')
                    key = input('Управляйте: ')
                    if key == 'h':
                        print('Лео: Молодец...Теперь не спеша возьми вон тот сейф который лежит на балконе,мои пацаны узнали это...')
                        print('Пользуйтесь той же клавишой - h чтобы взять маленький сейф')
                        key = input('Управляйте: ')
                        if key == 'h':
                            print('Лео: Всё...Теперь вали отсюда пока жители не узнали')
                            print('Подсказка: Пользуйтесь клавишой S чтобы уйти из дома')
                            
                            key = input('Управляйте: ')
                            if key == 's':
                                print('Вы идёте назад')
                                print('Вы: Всё,я принёс сейф')
                                time.sleep(5)
                                print('Лео: Отлично!Мои товарищи вскрыли этот сейф!Держи свою долю.Если нужна помощь в ограблениях я тебя жду)')
                                money += 10000
                                print('Ограбление успешно завершено!')
                                print(f'Баланс - {money}')
            if key == '2':
                braim_nps += 1
                print('Вы начали задание - ограбление ювелирного магазина')
                print('Лео: Привет!!!Я так понимаю ты встал на темную сторону? ')
                time.sleep(5)
                print('Вы: Ззздраввв ствуйте?)Вы кто? ')
                time.sleep(5)
                print('Лео: Я Лео - организатор всяких черных делишек.Мой братан мне сказал что ты хочешь ограбить ювелирный магазин...Это так?Я могу тебе помочь в этом')
                time.sleep(5)
                print('Вы: Да,я хочу!!!')
                print('Лео: Тогда пошли за мной,будем делать план')
                time.sleep(5)
                print('Лео: Итак,ты хочешь ограбить ювелирный магазин.Чтобы провернуть удачное ограбление выбери одно из двух действий.1 - Глупое,суть в том чтобы в открытую ограбить ювелирный магазин и через один проход уйти от полиции.2 - Умный,в умном ограблении нужно претвариться дезинсектором и через венциляцию кинуть усыпляющую гранату с газом.Ещё в умном ограблении нужно найти союзников,а именно водителя и хакера ')
                key = input('Выберите план ограбление 1.Глупое,2.Умное,написав номер в строку: ')
                if key == '1':
                    print('Лео: Ты выбрал план шумного ограбления!')
                    time.sleep(1)
                    print('Лео: Пока рано выдвигаться,уезжать от полиции мы всё таки будем не на ногах.Лучший транспорт для нашей ситуации является мотоцикл,я видел рядом с моим домом стоит один,так вот угони его')
                    print('Подсказка: Пользуйтесь клавишой E чтобы угнать мотоцикл')
                    key = input('Управляйте: ')
                    if key == 'e':
                        print('Вы угнали мотоцикл для ограбления')
                        print('Лео: Всё,ты угнал мотоцикл,молодец.Теперь надо оружие,но поскольку оно у меня есть погоди....Вот держи автомат,будешь его прикладом разбивать стекла в магазине и красть оттуда ювелирку')
                        time.sleep(5)
                        print('Лео: Выдвигайся')
                        time.sleep(3)
                        print('Вы: Так точно')
                        print('Подсказка: Вам нужно сесть в мотоцикл и поехать в ювелирный магазин.Пользуйтесь клавишой E')
                        if key == 'e':
                            print('Вы едете в ювелирный магазин...')
                            time.sleep(3)
                            print('Вы приехали в ювелирный магазин')
                            print('Лео: Ты прихеал.Теперь угрожай посетителям в ювелирном магазине и ломай стекла,как разбил воруй ювелирку')
                            time.sleep(3)
                            print('Вы: Всем лежать!!!Это ограбление,ты охранник тоже лежи')     
                            time.sleep(2)
                            print('*Сигнализация играет*')
                            print('Подсказка: Чтобы бить стекла пользуйтесь клавишой H')
                            key = input('Управляйте: ')
                            if key == 'h':
                                print('Вы разбили стекло и взяли ювелирку')
                                money += 5000
                                print(f'Куш: {money}')
                                print('Подсказка: Бейте стекла ещё')
                                key = input('Управляйте: ')
                                if key == 'h':
                                    print('Вы разбили стекло и взяли ювелирку')
                                    money += 5000
                                    print(f'Куш: {money}')
                                    print('Разбейте ещё одно стекло')
                                    key = input('Управляйте: ')
                                    if key == 'h':
                                        print('Вы разбили стекло и взяли ювелирку')
                                        money += 5000
                                        print(f'Куш: {money}')
                                        print('Лео: Садись на мотоцикл!!!Полиция уже на подходе!!!Поезжай туда куда я тебе скинул в телефоне...')
                                        print('Подсказка: Пользуйтесь клавишой E чтобы сесть в мотоцикл и ехать')
                                        key = input('Управляйте: ')
                                        if key == 'e':
                                            print('Вы едете по gps который вам скинул Лео')
                                            time.sleep(1)
                                            print('Вы едете по канализационным каналам')
                                            time.sleep(1)
                                            print('Вы приехали')
                                            print('Лео: Молодец!Отлично получилось,в этом ограблении я не кого не использовал,поэтому все 15000 твои!!!)))')
                                            money += 10000
                                            print('Ограбление успешно завершено!')
                                            print(f'Баланс: {money}')
                if key == '2':
                    print('Лео: Ты выбрал план умного ограбления')
                    time.sleep(5)
                    print('Лео: Тебе первое - набрать людей в команду,второе - угнать фургон для водителя,третье - найти газовую шашку,к слову газовую шашку нужно украсть у военной компании MaryWaezer')
                    arilles = ['Водитель','Хакер','Второй вор']
                    print(f'Твоя команда - {arilles}')
                    time.sleep(5)
                    print('Лео: Так,хорошо,первый пункт сделан ')
                    print('Лео: Теперь нужно угнать фургон для водителя.Поезжай вперед,он стоит рядом с дезинсекторами')
                    print('Подсказка: Сначала идите вперёд клавишой W')
                    key = input('Управляйте: ')
                    if key == 'w':
                        print('Подсказка: Отлично!Теперь пользуйтесь клавишой E для того чтобы угнать фургон')
                        key = input('Управляйте: ')
                        if key == 'e':
                            print('Подсказка: Вы успешно угнали фургон')
                            print('Лео: Всё,отлично,теперь надо украсть газовую шашку у военной компании - MaryWaezer.Она на складе завода GunsForWaezer,этот завод поставляет оружие этой военной компании.Сейчас жди время,лучшее время для этого ночь')
                            for i in range(16, 23):
                                time.sleep(0.5)
                                print(f'Время идёт - {i}')
                            print('Лео: Самое время своровать газовую шашку на складе завода.Местоположение кинул в gps твоего телефона ')
                            print('Подсказка: Угоните любое транспортное средство - клавиша E,чтобы было удобно быстро сделать пункт из плана')
                            key = input('Управляйте: ')
                            if key == 'e':
                                print('Вы едете на склад завода GunsForWaezer')
                                time.sleep(2)
                                print('Подсказка: Вы успешно приехали')
                                print('Лео: Без резких движений открывай дверь склада отмычкой,пока мы с тобой составляли план я сунул тебе её в карман')
                                print('Подсказка: Чтобы взломать дверь пользуйтесь клавишой - H')
                                key = input('Управляйте: ')
                                if key == 'h':
                                    print('Вы успешно взломали дверь')
                                    print('Лео: Всё идёт как по маслу,в ящике лежит газовая шашка')
                                    time.sleep(0.5)
                                    print('Вы украли газовую шашку')
                                    print('Вы едете обратно в офис к Лео')
                                    time.sleep(0.5)
                                    print('Вы приехали')
                                    print('Лео: Отлично!Ты сделал всё из нашего плана.Теперь пора брать команду и выдвигаться на дело')
                                    print('Лео: И ещё,говорю,действия я буду говорить тебе в наушник')
                                    time.sleep(0.5)
                                    print('Водитель отвёз вашу команду на дело')
                                    time.sleep(0.5)
                                    print('Лео: Алло привет!Это я - Лео.Видишь вон ту лестнецу?Так вот поднимайся по ней на крышу')
                                    print('Подсказка: Чтобы подняться по лестнеце клавиша - W')
                                    key = input('Управляйте: ')
                                    if key == 'w':
                                        print('Вы поднялись')
                                        print('Лео: Молодец!Теперь кидай в вентиляцию газовую шашку')
                                        print('Подсказка: Чтобы кинуть газовую шашку клавиша - H')
                                        key = input('Управляйте: ')
                                        if key == 'h':
                                            print('Вы кинули газовую шашку')
                                            print('Лео: Подожди пока люди в ювелирном магазине подышали газом и уснули')
                                            time.sleep(0.5)
                                            print('Лео: Все люди уснули теперь пора бить стёкла.Не думай что сигнализация будет играть,её отключил хакер из команды')
                                            print('Подсказка: Чтобы бить стекла пользуйтесь клавишой H')
                                            key = input('Управляйте: ')
                                            if key == 'h':
                                                print('Вы разбили стекло и взяли ювелирку')
                                                money += 5000
                                                print(f'Куш: {money}')
                                                print('Подсказка: Бейте стекла ещё')
                                                key = input('Управляйте: ')
                                                if key == 'h':
                                                    print('Вы разбили стекло и взяли ювелирку')
                                                    money += 5000
                                                    print(f'Куш: {money}')
                                                    print('Разбейте ещё одно стекло')
                                                    key = input('Управляйте: ')
                                                    if key == 'h':
                                                        print('Вы разбили стекло и взяли ювелирку')
                                                        money += 5000
                                                        print(f'Куш: {money}')
                                                        print('*Сигнализация играет*')
                                                        time.sleep(0.5)
                                                        print('Уезжай теперь к чертям оттуда.Туда едет полиция.Водитель у нас опытный и он быстро уедет')
                                                        print('Вы уехали')
                                                        time.sleep(1)
                                                        print('Вы приехали,полиция не поймала!')
                                                        print('Лео: Молодец!Я поделил деньги и у ты заработал с ограбления 15000')
                                                        print('Ограбление успешно завершнено!')
                                                        print(f'Баланс: {money}')

            if key == '3':
                braim_nps += 1
                print('Вы начали задание ограбление банка')
                time.sleep(5)
                print('Лео: Привет!!!Я так понимаю ты встал на темную сторону? ')
                time.sleep(5)
                print('Вы: Ззздраввв ствуйте?)Вы кто? ')
                time.sleep(5)
                print('Лео: Я Лео - организатор всяких черных делишек.Мой братан мне сказал что ты хочешь ограбить банк...Это так?Я могу тебе помочь в этом')
                time.sleep(5)
                print('Вы: Да,я хочу!!!')
                time.sleep(5)
                print('Лео: Тогда пошли за мной,будем делать план')
                time.sleep(5)
                print('Лео: Для того чтобы ограбить банк нужно - сумка,она у меня есть,я тебе дам,второе - бомба-липучка,пистолет с глушителем,эти предметы я тоже дам')
                print('Лео: Дело идёт об ограблении банка,значит нужно действовать аккуратно и следовать моим инструкциям')
                print('Лео: Не волнуйся я с тобой,только по наушнику')
                print('Подсказка: Идите в банк клавиша - w')
                key = input('Управляйте: ')
                if key == 'w':
                    print('Вы пришли в банк')
                    print('Лео: Поднимайся по лестнеце и выруби все камеры пистолетом')
                    print('Подсказка: чтобы подняться по лестнеце которая ведёт на крышу клавиша - H')
                    key = input('Управляйте: ')
                    if key == 'h':
                        print('Вы поднялись по лестнеце')
                        print('Подсказка: Теперь вырубите камеры рядом с сейфом клавиша - H')
                        key = input('Управляйте: ')
                        if key == 'h':
                            print('Вы вырубили все камеры вокруг сейфа')
                            print('Лео: Хорош!Теперь бросай бомбу-липучку на сейф..Помни,за тобой на вертолёте прилетит команда и вытащит тебя')
                            print('Подсказка: Чтобы кинуть бомбу-липучку клавиша - g')
                            key = input('Управляйте: ')
                            if key == 'g':
                                print('Бомба на сейфе...')
                                time.sleep(2)
                                print('Сейф открыт')
                                money += 30000
                                print('Вы украли 30000')
                                print('*Сигнализация играет*')
                                time.sleep(0.5)
                                print('Лео: Уходи быстро так же по лестнеце мои пацаны на вертлёте ждут тебя')
                                time.sleep(1)
                                print('Вы забрались на вертолёт и улетели')
                                time.sleep(1)
                                print('Лео: Молодчина!Ограбление прошло удачно.Чистыми ты заработал 20000!Остальные 10000 ушли моим пацанам за помощь тебе')
                                print('Ограбление успешно завершено!')
                                print(f'Баланс: {money}')

