



name_day = ( 
    "Понедельник", "Вторник", "Среда",
    "Четверг", "Пятница", "Суббота", "Воскресенье",
) # Название дней


for i in range(7):
    print(f"№ дня: {i + 1}. Название дня: {name_day[i]}.  \t Это {'выходной день.' if i + 1 > 5 else 'рабочий день.'}")
    # \t - Tab (для более приятного вывода)