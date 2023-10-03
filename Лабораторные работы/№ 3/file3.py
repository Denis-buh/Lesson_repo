



def in_degree(number:int, degree:float) -> None:
    """Процедура, которая вычисляет степень числа 

    Args:
        number (int): передаваемое число
        degree (float): передаваемая степень

    """
    if number < 0 and (degree ** (-1)) % 2 == 0:
        print("Невозможно из отрицательного числа вычислить четный корень")
    
    print("Число в степени", number ** degree)


if __name__ == "__main__": # Если скрипт запущен как основной
    in_degree(int(input("Введите число: ")), 
              float(input("Введите степень числа: ")))

