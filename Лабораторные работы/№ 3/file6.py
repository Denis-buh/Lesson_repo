



def factorial(N:int) -> int:
    """Функция, которая вычисляет факториал натурального числа  N

    Args:
        N (int): передаваемое число

    Returns:
        int: факториал числа
    """
    if N < 0:
        return "Факториал нельзя расчитать"
    
    if N in (0, 1):
        return 1
    
    fk = 1
    for i in range(1, N+1):
        fk *= i
        
    return fk


if __name__ == "__main__": # Если скрипт запущен как основной
    print("Факториал числа:", factorial(int(input("Введите число: "))))
    
    
    def Test():
        tests = [(0, ), (-25, ), (1, ), (6, )]
        result = [1, "Факториал нельзя расчитать", 1, 720]
        k = 0
        for i in tests:
            res = factorial(*i)
            assert  res == result[k], f"Test {k}: answer: {res} good answer: {result[k]}"
            k += 1
        
    # Test()