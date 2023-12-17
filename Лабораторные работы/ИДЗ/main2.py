



def fun(x):
    if x < -4.5:
        r1 = (9 * (x ** 2)) + 5
        r2 = (3 * x) + 12
        return r1 / r2
    elif x >= -4:
        return (4 * (x ** 2)) - 7
    else:
        return "Введено число в диапозоне [-4.5; -4)"


def main():
    x = int(input("Введите значение x: "))
    print(f"Результат: {fun(x)}")
    

if __name__ == "__main__":
    main()