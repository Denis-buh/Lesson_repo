



def fibonacci(N:int) -> None:
    """Поиск и вывод чисел фибоначи

    Args:
        N (int): натуральное число 
    """
    if N < 0:
        print("Число должно быть натуральным")
        return

    print("Ряд фибоначи:")
    
    if 0 <= N < 1:
        print(0)
        return
    
    n_pas, n_new = 1, 1
    for i in range(N):
        print(n_pas)
        n_new, n_pas = n_new + n_pas, n_new


if __name__ == "__main__": # Если скрипт запущен как основной
    fibonacci(int(input("Введите число N: ")))
    