



lst = [] # Список для хранения будующих данных

for i in range(10):
    lst.append(int(input("Введите число: ")))
    
lst.sort()
# print(lst)
for i in lst:
    if i % 2 == 0 and i % 3 != 0:
        print(f"Вот это число: {i}")
        break
else:
    print("Такое число не было введено")
