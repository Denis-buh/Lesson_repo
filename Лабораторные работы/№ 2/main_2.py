



number = input("Введите число: ")

flag = 0

for i in number:
    if int(i) % 4 == 0:
        flag += 1
        
print(f"Колличество цифр кратных 4: {flag}")