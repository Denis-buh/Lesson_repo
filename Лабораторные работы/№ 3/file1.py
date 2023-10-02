



def number_col(number:float) -> None:
    """Процедура которая выводит на экран в столбик все цифры переданного ей числа (начиная с последней).

    Args:
        number (float): переданное число
    """
    if number == int(number):
        number = int(number)
    
    number = str(abs(number))[::-1]
    print("Цифры переданного числа: ")
    for i in number:
        if i == ".":
            continue
        print(i)


if __name__ == "__main__": # Если скрипт запущен как основной
    number_col(float(input("Введите число: ")))
