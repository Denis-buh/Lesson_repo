



def main():
    '''Функция main'''
    st = input("Введите строку: ")
    print(f"Ваши символы с четными номерами: {list(st[1::2])}")
    print(f"Ваши символы с не четными номерами: {list(st[::2])}")
    
    
if __name__ == "__main__":
    main()