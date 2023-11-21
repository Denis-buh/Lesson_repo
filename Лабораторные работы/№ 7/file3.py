



import random


def main():
    '''Функция main'''
    ls = []
    LEN = 20
    for i in range(LEN):
        ls.append(random.randint(0, 4))
    min_item_index = ls.index(min(ls))
    max_item_index = ls.index(max(ls))
    print(f"Номер первого минимального элемента массива {min_item_index + 1}")
    print(f"Номер последнего максимального элемента массива {max_item_index + 1}")
    


if __name__ == "__main__":
    main()