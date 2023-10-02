



def in_degree(number:int, degree:float) -> int:
    """Процедура, которая вычисляет степень числа 

    Args:
        number (int): передаваемое число
        degree (float): передаваемая степень

    Returns:
        int: число в степени
    """
    if number < 0 and (degree ** (-1)) % 2 == 0:
        return "Невозможно из отрицательного числа вычислить четный корень"
    
    return number ** degree


if __name__ == "__main__": # Если скрипт запущен как основной
    print(in_degree(int(input("Введите число: ")), 
                    float(input("Введите степень числа: "))
                    )
          )
    
    
    def Test():
        tests = [(7, 2), (-25, 0.5), (205, 0.5)]
        result = [49, "Невозможно из отрицательного числа вычислить четный корень", 5]
        k = 0
        print("Tests")
        for i in tests:
            res = in_degree(*i)
            assert  res == result[k], f"Test {k}"
            k += 1
        
    # Test()