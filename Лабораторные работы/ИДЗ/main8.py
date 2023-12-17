



def main():
    count_number = int(input("Введите количество цифр: "))
    sp = [] # список для оценок
    for i in range(count_number):
        sp.append(int(input("Введите значение оценки: ")))
    
    print(f"Среднее арифметическое {round(sum(sp) / len(sp), 3)}")
    
    
if __name__ == "__main__":
    main()