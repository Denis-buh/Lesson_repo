



def main():
    '''Функция main'''
    ls = []
    LEN = int(input("Введите длину массива: "))
    for i in range(LEN):
        ls.append(float(input("Введите значение элента: ")))


    print(f"Введеный массив: {ls}")
    print(f"Номера элементов  в возрастающем порядке: {[ls.index(i) + 1 for i in sorted(ls)]}")


if __name__ == "__main__":
    main()