



def main():
    '''Функция main'''
    roat_to_file = input("Введите путь к файлу: ")
    if "\\" in roat_to_file:
        roat_to_file = roat_to_file.replace("\\", "/")
    
    roat_to_file = roat_to_file.split("/")
    for i in roat_to_file:
        print(i)
    
    
if __name__ == "__main__":
    main()