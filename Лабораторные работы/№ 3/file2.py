



def divider(number:int) -> None:
    """Процедуру, которая определяет все делители передаваемого ей числа (в одну строчку)

    Args:
        number (int): передаваемое число

    """
    res = ""
    for i in range(1, abs(number)+1):
        if number % i == 0:
            res += f"{i} "
            
    if len(res) == 0:
        print("Таких чисел нет")
    print("Делители:", res)


if __name__ == "__main__": # Если скрипт запущен как основной
    divider(int(input("Введите число: ")))
