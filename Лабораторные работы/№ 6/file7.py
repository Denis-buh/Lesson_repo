



def main():
    '''Функция main'''
    my_list = []

    while True:
        number = input("Введите значение для элемента списка (break - остановка ввода): ")
        if number == "break":  break
        my_list.append(float(number))
    
    range_min = float(input("Введите минимальное значение для диапазона: "))
    range_max = float(input("Введите максимальное значение для диапазона: "))
    cout = int(input("Введите количество элементов: "))
    
    ls_ind = []
    for i in range(len(my_list)):
        if (range_min <= my_list[i] <= range_max) and cout:
            ls_ind.append(str(i))
            my_list[i] = False # Удаляем элемент из списка
            cout -= 1
        elif not cout:
            break
        
    print(f"Индексы элементов поподающие в диапазон: {' '.join(ls_ind)}")


if __name__ == "__main__":
    main()