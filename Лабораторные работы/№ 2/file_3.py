



lst = () # Список для хранения будущих данных

for i in range(10):
    lst += int(input("Введите число: ")),  # Добавляем введенное число в список
    

lst_sorted = ()
for i in range(10): # Сортируем список от меньшего к большему
    lst_sorted += min(lst), 
    lst = lst[:lst.index(min(lst))] + lst[lst.index(min(lst)) + 1:]

for i in lst_sorted:
    if i % 2 == 0 and i % 3 != 0:
        print(f"Вот это число: {i}")
        break # Прекращаем цикл так как было найдено число
else:
    print("Такое число не было введено")
