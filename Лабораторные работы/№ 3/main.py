



def found_pall(number:str) -> bool:
    return number == number[::-1]


def main():
    k = 0
    for i in range(int(input("Введите количество элементов в последовательности: "))):
        number = input("Введите значение элемента: ")
        if found_pall(number):
            k += 1
    print(f"Количество палиндромов: {k}")


if __name__ == "__main__":
    main()

