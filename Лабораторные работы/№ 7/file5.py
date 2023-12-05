



def quick_sort(A, nStart, nEnd) -> list:
    if nStart >= nEnd: return
    L = nStart; R = nEnd
    X = A[(L+R)//2]
    while L <= R:
        while A[L] < X: L += 1 # разделение
        while A[R] > X: R -= 1
        if L <= R:
            A[L], A[R] = A[R], A[L]
        L += 1; R -= 1
        quick_sort( A, nStart, R ) # рекурсивные вызовы
        quick_sort( A, L, nEnd )

    
def main():
    '''Функция main'''
    ls = []
    LEN = int(input("Введите длину массива: "))
    for i in range(LEN):
        ls.append(float(input("Введите значение элента: ")))
    print(f"Массив до сортировки: {ls}")
    quick_sort(ls, 0, LEN - 1) 
    print(f"Массив после сортировки: {ls}")


if __name__ == "__main__":
    main()