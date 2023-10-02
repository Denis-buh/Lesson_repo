



def divider(number:int) -> str:
    """Процедуру, которая определяет все делители передаваемого ей числа (в одну строчку)

    Args:
        number (int): передаваемое число

    Returns:
        str: строка с делителями
    """
    res = ""
    for i in range(1, abs(number)+1):
        if number % i == 0:
            res += f"{i} "
            
    if len(res) == 0:
        return "Таких чисел нет"
    return res


if __name__ == "__main__": # Если скрипт запущен как основной
    print("Делители:", divider(int(input("Введите число: "))))
    
    
    def Test():
        tests = [(7, ), (-5, ), (0, )]
        result = ["1 7 ", "1 5 ", "Таких чисел нет"]
        k = 0
        for i in tests:
            res = divider(*i)
            assert  res == result[k], f"Test {k}"
            k += 1
    
    
    # Test()