



import math


x = float(input('Введите x: '))

if x <= 1:
    print("Были введены не верные данные")
    
else:
    n = 0 # Количество итераций цикла
    # Точность предела последовательности
    e =  0.0000005 
    # Прошлый элемент последовательности
    a_past = float(input('Введите a0: ')) 
    while True:
        n += 1
        # Новый элемент последовательности
        a_next = 1 + math.sin(1 + (a_past ** 2)) / x ** n 
        
        if abs(a_past - a_next) < e:
            print(f"Найденый предел последовательности: {a_next}")
            break
        a_past = a_next
