




N = 10
lst_sum = [] # Список для хранения будующих данных
for i in range(N):
    lst_sum.append(int(input("Введите количество случайных цифр: ")))
    
print(f"Среднее арифметическое: {sum(lst_sum) / len(lst_sum)}")