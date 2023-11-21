



def check_easy(number:int) -> bool:
    """Проверка на числа на простоту
    Args:
        number(int): Строка для проверки
    """
    sqrt_number = abs(number) ** (1/2) # Находим корень для числа
    
    if sqrt_number == int(sqrt_number):  return False
    for i in range(2, int(sqrt_number) + 1):
        if number % i == 0:  return False
        
    return True    


def main():
    '''Функция main'''
    ls = input("Введите значения для массива (через ; ): ").split(";")
    
    ls_easy = []
    for i in ls:
        if check_easy(int(i)):  ls_easy.append(i)
    print(f"Простые числа: {' '.join(ls_easy)}")


if __name__ == "__main__":
    main()