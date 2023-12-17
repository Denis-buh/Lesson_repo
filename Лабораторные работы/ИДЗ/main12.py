



def main():
    '''Функция main'''
    
    while True:
        st = input("Введите строку (break для завершения ввода): ")
        if st == "break":
            return
        
        print(f"Строка до преобразований: {st}")
        st = st.replace(",", " ")
        print(f"Строка после преобразований: {st}")


if __name__ == "__main__":
    main()
