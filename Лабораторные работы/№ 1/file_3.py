



count_clok = float(input("Введите колличество отработанных часов: "))
cost_clok = float(input("Введите заработок в час: "))
k = 1 # коэффициент зп

if count_clok > 40:
    k = 1.5
    
print("Ваша зарплата: {0}".format(count_clok * cost_clok * k))