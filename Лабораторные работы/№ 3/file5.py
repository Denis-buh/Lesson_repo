



def len_number(number:float) -> int:
    """Процедура, которая вычисляет количество цифр числа

    Args:
        number (float): передаваемое число

    Returns:
        int: количество цифр числа
    """
    number = abs(number) # Убираем знак числа
    k = 1 # Коофицент количества служебных знаков
    if number == int(number):
        k = 2
        
    return len(str(number)) - k


if __name__ == "__main__": # Если скрипт запущен как основной
    print("Количество цифр числа:", len_number(float(input("Введите число: "))))
    
    
    def Test():
        tests = [(123.0, ), (-25.0, ), (0.0, ), (2.4, )]
        result = [3, 2, 1, 2]
        k = 0
        for i in tests:
            res = len_number(*i)
            assert  res == result[k], f"Test {k}: answer: {res} good answer: {result[k]}"
            k += 1
        
    # Test()