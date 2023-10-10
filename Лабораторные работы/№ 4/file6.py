



import random

number_of_t = int(input('Введите количество раз:'))
n = 0
sum_ch = 0
sum_nech = 0

lst = [random.randint(20,100) for a in range (number_of_t)]
for b in range(len(lst)):
    number = lst [b]
    number = int(number)
    if number % 2 == 0:
        sum_ch += number
    else:
        sum_nech += number

print('Сумма чётных элементов: {0}, сумма нечётных элементов: {1}'.format(sum_ch,sum_nech))
