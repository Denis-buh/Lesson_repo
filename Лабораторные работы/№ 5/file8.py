



def main():
    '''Функция main'''
    S = input("Введите строку: ")
    L = len(S)
    flag = True
    for i in range(1, L // 2):
        if S[i - 1] == S[L - i]:
            k = True
        else:
            k = False
        flag = flag * k
    
    if flag:
        res = "Палиндром"
    else:
        res = "Не палиндром"
    
    print(res)


if __name__ == "__main__":
    main()