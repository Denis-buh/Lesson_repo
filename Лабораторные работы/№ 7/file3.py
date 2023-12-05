



import random


def main():
    '''Функция main'''
    ls = []
    LEN = 20
    for i in range(LEN):
        ls.append(random.randint(0, 4))
        
    min_item_index = None
    max_item_index = None
    for i in range(len(ls) - 1):
        if min_item_index == None and ls[i] < ls[i+1]:
            min_item_index = i
            
        if ls[i] > ls[i+1]:
            max_item_index = i
    print(f"Массив: {ls}")
    print(f"Номер первого минимального элемента массива {min_item_index + 1}")
    print(f"Номер последнего максимального элемента массива {max_item_index + 1}")
    


if __name__ == "__main__":
    main()