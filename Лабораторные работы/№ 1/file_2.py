



import math


x = float(input("Введите значение первой переменной: "))
y = float(input("Введите значение второй переменной: "))

print("Сумма чисел {0} и {1} = {2}".format(x, y, x + y))
print("Разность чисел {0} и {1} = {2}".format(x, y, x - y))
print("Произведение чисел {0} и {1} = {2}".format(x, y, x * y))
print("Частное чисел {0} и {1} = {2}".format(x, y, x / y))
print("Целочисленное деление чисел {0} и {1} = {2}".format(x, y, x // y))
print("Остаток от целочисленного деления чисел {0} и {1} = {2}".format(x, y, x % y))
print("Возвидение числа {0} в {1} степень = {2}".format(x, y, x ** y))
print("Модуль числа |{0}| = {1} и числа |{2}| = {3}".format(x, abs(x), y, abs(y)))
print("Округленые числа {0}, {1}".format(round(x), round(y)))
print("Квадратный корень 1 переменной = {0} и 2 переменной = {1}".format(math.sqrt(x), math.sqrt(y)))
print("Экспонента 1 переменной = {0} и 2 переменной = {1}".format(math.exp(x), math.exp(y)))
print("Натуральный логарифм 1 переменной = {0} и 2 переменной = {1}".format(math.log(x), math.log(y)))
print("В двоичной системе счисления 1 переменная = {0} и 2 переменная = {1}".format(bin(int(x)), bin(int(y))))
print("В восьмеричной системе счисления 1 переменная = {0} и 2 переменная = {1}".format(oct(int(x)), oct(int(y))))
print("В шестнадцатеричной системе счисления 1 переменная = {0} и 2 переменная = {1}".format(hex(int(x)), hex(int(y))))
