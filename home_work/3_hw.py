print('Задача №1')
def max_number(a, b):
    return max(a,b)

print(max_number(3, 5))
print(max_number(4, 4))


print('\nЗадача №2')
def gap_between_numbers(a, b) -> str:
    if abs(a-b) == 135:
        print('Yes')
    else:
        print('No')

gap_between_numbers(1,136)
gap_between_numbers(1,137)


print('\nЗадача №3')
def month_season(month: int) -> str:
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        raise ValueError("Номер месяца должен быть целым числом от 1 до 12")

print(month_season(1))
print(month_season(3))
print(month_season(6))
print(month_season(11))
# print(month_season('p'))


print('\nЗадача №4')
def greater_ten(a, b, c) -> str:
    if  a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('No')

greater_ten(12,11,5)
greater_ten(12,11,13)
greater_ten(12,11,10)


print('\nЗадача №5')
def count_pos_numbers(list: list) -> int:
    if len(list) == 5:
        count = 0
        for elem in list:
            if elem > 0:
                count += 1
        return count
    else:
        raise ValueError("Список должен содержать ровно 5 элементов")

print(count_pos_numbers([5, -3, 0, 4, -7]))


print('\nЗадача №6')
def calculate_age_in_days(years: int, months: int) -> int:
    if years >= 0 and months >=0:
        return (years * 12 + months) * 29
    else:
        raise ValueError("Количество лет и месяцев должны быть неотрицательными целыми числами")
    
print(calculate_age_in_days(5, 3))