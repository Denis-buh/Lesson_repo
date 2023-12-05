



def my_fun(arr):
    LEN = len(arr)
    sp_set = []
    for i in range(LEN):
        itr = LEN - i - 1
        for ii in range(itr):
            if arr[ii] > arr[ii + 1]:
                arr[ii + 1], arr[ii] = arr[ii], arr[ii + 1]  
        if arr[i] not in sp_set:
            sp_set.append(arr[i])
    return arr, len(sp_set)


def main():
    '''Функция main'''
    ls = []
    LEN = int(input("Введите длину массива: "))
    for i in range(LEN):
        ls.append(float(input("Введите значение элента: ")))
        
    print(f"Введеный массив: {ls}")
    arr, sp_set = my_fun(ls)
    print(f"Отсортированный массив: {arr}")
    if sp_set == 1:
        print(f"Количество различных чисел в массиве: {sp_set}")
    else:
        print("Количество различных чисел в массиве: их нет")


if __name__ == "__main__":
    main()