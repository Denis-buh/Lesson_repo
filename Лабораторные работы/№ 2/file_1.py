



sum_number_pos = 0 # Переменные для хранения значения
sum_number_neg = 0 # Переменные для хранения значения

while True:
    number = int(input("Введите число: "))
    if number == 0:
        break
    
    if number > 0:
        sum_number_pos += number
    elif number < 0:
        sum_number_neg += number
    
print(f"Сумма положительных: {sum_number_pos}")
print(f"Сумма отрицательных: {sum_number_neg}")
