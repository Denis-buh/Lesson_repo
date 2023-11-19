



def main():
    '''Функция main'''
    my_list = []
    N = int(input("Введите количество элементов списка: "))
    for i in range(N):
        my_list.append(float(input("Введите значение для элемента списка: ")))
    print(f"Среднее значение для списка {sum(my_list) / N}")


if __name__ == "__main__":
    main()