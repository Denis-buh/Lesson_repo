



def progres(a_1, n, d):
    return a_1 + ((n - 1) * d)


def main():
    a_1 = float(input("Введите первый элемент ариф. прогрессии: "))
    d = float(input("Введите разность ариф. прогрессии: "))
    n = int(input("Введите количество элементов ариф. прогрессии: "))
    lst = []
    for n in range(1, n + 1):
        a_new = progres(a_1, n, d)
        lst.append(a_new)
        
    print(f"Массив с арифм. прогрессией: \n{lst}")
    
    
if __name__ == "__main__":
    main()