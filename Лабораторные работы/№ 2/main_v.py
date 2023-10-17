



number = input("Введите число: ")

number_ch = 0
number_nech = 0

for i in number:
    if int(i) % 2 == 0:
        number_ch += 1
    else:
        number_nech +=1
        
print(f"Колличество чётных цифр: {number_ch}\nКоличество нечётных: {number_nech}")