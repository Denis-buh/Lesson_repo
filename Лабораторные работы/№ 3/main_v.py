



def check_digits_in_number(number):
    number = str(number)
    return (number.count("0"), number.count("1"))


while True:
    number = float(input("Введи число: "))
    
    if number == 0:
        break
    
    if number < 0 or number != int(number):
        print("Введено не верное значение")
        
    else:
        res = check_digits_in_number(int(number))
        print(f"Количество 0: {res[0]} \nКоличество 1: {res[1]}\n")
    
        