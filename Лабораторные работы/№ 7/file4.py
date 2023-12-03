



def main():
    '''Функция main'''
    ls = []
    LEN = int(input("Введите длину массива: "))
    for i in range(LEN):
        ls.append(float(input("Введите значение элента: ")))
    
    print(f"Массив до сортировки: {ls}")
    for i in range(LEN):
        itr = LEN - i - 1
        for ii in range(itr):
            if ls[ii] > ls[ii + 1]:
                ls[ii + 1], ls[ii] = ls[ii], ls[ii + 1]
    print(f"Массив после сортировки: {ls}")


if __name__ == "__main__":
    main()