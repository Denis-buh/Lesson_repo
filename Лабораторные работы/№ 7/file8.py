



def my_fun(arr):
    res = []
    flag = [arr[0], 1]
    for i in arr[1:]:
        if i == flag[0]:
            flag[1] += 1
        else:
            res.append(flag)
            flag = [i, 1]
    return res


def main():
    '''Функция main'''
    ls = []
    
    LEN = int(input("Введите длину массива: "))
    for i in range(LEN):
        ls.append(float(input("Введите значение элента: ")))

    print(f"Введеный массив: {ls}")
    res = my_fun(ls)
    print(f"Значения элементов образующие серии: {[i[0] for i in res]}")
    print(f"Длины всех серий одинаковых элементов: {[i[1] for i in res]}")


if __name__ == "__main__":
    main()