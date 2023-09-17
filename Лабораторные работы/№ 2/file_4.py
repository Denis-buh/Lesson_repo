




N = 10
lst_sum = [] # Список для хранения будущих данных
for i in range(N):
    lst_sum.append(int(input("Введите значение цифры: ")))
    
print(f"Среднее арифметическое: {sum(lst_sum) / len(lst_sum)}")
