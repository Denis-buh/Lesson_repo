



def made_mtr(st, col):
    A = []
    for i in range(st):
        sp = []
        for ii in range(col):
            sp.append(int(input(f"Введите значение элемента с номером {i + 1, ii + 1}: ")))
        A.append(sp)
    return A


def mtr_command(A):
    for i in range(len(A[0])):
        sp = []
        for ii in range(len(A)):
            sp.append(A[ii][i])
        ind_max = sp.index(max(sp))
        res = 1
        for g in sp:
            if g < 0:  res *= g
        A[ind_max][i] = res


def __str(A):
    arr = []
    for i in range(len(A)):
        arr.append(" ".join([str(ii) for ii in A[i]]))
    arr = '\n'.join(arr)
    return arr


def main():
    st = int(input("Введите количество строк матрицы: "))
    col = int(input("Введите количество колонок матрицы: "))
    A = made_mtr(st, col)

    print(f"Введеная матрица:\n{__str(A)}")
    mtr_command(A)
    print(f"Обработанная матрица:\n{__str(A)}")
    
    
if __name__ == "__main__":
    main()
    
