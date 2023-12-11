



import sys, os


def wright_file() -> None:
    file = open("test.txt", "w")
    sp = []
    
    while True:
        number = input("Введите число (break - остановка ввода): ")
        if number == "break":
            break
        sp.append(number)
    
    file.write("\n".join(sp))
    file.close()


def read_file() -> None:
    file = open("test.txt", "r")
    sp = [int(i) for i in file.readlines()]
    file.close()
    big_numbers, low_number = [], []
    cout_sero_number = 0
    
    for i in sp:
        if i > 10:
            big_numbers.append(i)
        elif i == 0:
            cout_sero_number += 1
        elif i < 2:
            low_number.append(i)
    
    print(f"Числа больше 10: {big_numbers}")
    print(f"Числа меньше 2: {low_number}")
    print(f"Числа равные 0: {cout_sero_number}")
    
    


# Особенноесть среды разработки
PROGRAM_DIR = "\\".join(sys.argv[0].split("\\")[:-1]) # Папка программы
os.chdir(PROGRAM_DIR) # Переход в папку программы


def main():
    #wright_file()
    read_file()
    
    
    
    
if __name__ == "__main__":
    main()