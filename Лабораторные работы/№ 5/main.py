



def main():
    '''Функция main'''
    x = []
    while True:
        number = input("Введите число (break - остановка): ").rstrip('\n')
        if number == "break":
            break
        
        x.append(float(number))
            
    print(f"Полученный список {x}") 
    Y = []
    
    for i in x:
        if 1 <= i <= 2:
            Y.append(i)
    if len(Y) <= 1:
        print(f"Полученный список c элементами с из диапазона [1, 2]: {Y}")
        return
        
    in_max = Y.index(max(Y))
    in_min = Y.index(min(Y))
    
    Y[in_min], Y[in_max] = max(Y), min(Y) 
    print(f"Полученный список c элементами с из диапазона [1, 2]: {Y}") 


if __name__ == "__main__":
    main()
    
