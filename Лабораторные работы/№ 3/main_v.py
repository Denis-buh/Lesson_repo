



number_ext = int


def amount_of_0_and_1(number: int) -> int:
    global number_ext
    number_ext = number
    number = str(number)
    if True:
        return number.count('1'), number.count('0')


while True:
    print(amount_of_0_and_1(int(input("Введите число: "))))
    if number_ext == 0:
        break

    
        