



import random


N = 10 # количество итераций цикла
lst_sum = [] # Список для хранения будущих данных
for i in range(N):
    lst_sum.append(random.randint(0, 1_000))
    
print(f"Среднее арифметическое случайных чисел: {sum(lst_sum) / len(lst_sum)}")