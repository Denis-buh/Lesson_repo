



import random


def main():
    '''Функция main'''
    ls = []
    LEN = 20
    for i in range(LEN):
        ls.append(random.randint(0, 4))
    X = float(input("введите значение X: "))
    ls_ind = []
    for i in range(LEN):
        if ls[i] == X:
            ls_ind.append(str(i))    
    print(f"Номера элементов, равных значению X: {'Их нет' if len(ls_ind) == 0 else ' '.join(ls_ind) }")


if __name__ == "__main__":
    main()