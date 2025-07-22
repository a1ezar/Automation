num = 3

if num >= 0:
    print("число больше либо равно 0")
else:
    print("число отрицательное")

def task_yes_no(str_1, str_2):
    if str_1 in str_2:
        print("ДА")
    else:
        print("НЕТ")

task_yes_no(str_1='test', str_2='test1')

num_float = 3.4

# num_float = 0
# num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')
    
a = -101
if abs(a) > 100:
    print('-')
else:
    print('+')