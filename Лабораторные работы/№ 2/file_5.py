



import random


N = 10 # количество итераций цикла
lst_sum = 0 # Список для хранения будущих данных
for i in range(N):
    lst_sum += random.randint(0, 1_000)
    
print(f"Среднее арифметическое случайных чисел: {lst_sum / N}")