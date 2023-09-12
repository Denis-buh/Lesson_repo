



import random


N = 10
lst_sum = [] # Список для хранения будующих данных
for i in range(N):
    lst_sum.append(random.randint(-1_000, 1_000))
    
print(f"Среднее арифметическое: {sum(lst_sum) / len(lst_sum)}")