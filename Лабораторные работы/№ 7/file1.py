



def main():
    '''Функция main'''
    ls = []
    while True:
        number = input("Введите значение для элемента списка (break - остановка ввода): ")
        if number == "break":  break
        ls.append(float(number))
    for i in ls:
        if i % 3 == 0:
            print(f"Введенный маcсив: {ls}")
            print("В  массиве есть числа, кратные трем.")
            break


if __name__ == "__main__":
    main()