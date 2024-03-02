def season(month):
    if month in [1,11,12]:
        return 'зима'
    elif month in [3,4,5]:
        return 'весна'
    elif month in [6,7,8]:
        return 'лето'
    elif month in [9,10,11]:
        return 'осень'
    

month = input('Введите номер месяца: ')
month = int(month)
print(season(month))




def cel_to_far(cel):
    return cel * (9/5) + 32
print(cel_to_far(25))