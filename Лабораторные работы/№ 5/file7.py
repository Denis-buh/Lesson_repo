



def main():
    '''Функция main'''
    prim = input("Введите выражение: ")
    prim = [int(i) for i in prim.split("+")]
    print(f"Сумма выражения: {sum(prim)}")
    
    
if __name__ == "__main__":
    main()