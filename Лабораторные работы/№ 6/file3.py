



import copy


def check_palid(st:str) -> bool:
    """Проверка на палидром

    Args:
        st (str): Строка для проверки
    """
    lst_new = copy.deepcopy(st)
    lst_new = lst_new[::-1]
    return st == lst_new


def main():
    '''Функция main'''
    stroka =  input('Введите слово: ') 
    lst = list(stroka) # конвертируем строку в список 
    if check_palid(lst):
        print("Введенная строка - палидром")
    else:
        print("Введенная строка - не палидром")


if __name__ == "__main__":
    main()