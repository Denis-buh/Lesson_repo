



def __init__(n, m):
    itm = []
    for i in range(n):
        st = []
        for ii in range(m):
            st.append(float(input(f"Введите значение для элемента [{i+1, ii+1}]")))
        itm.append(st)
    return itm
    
    
def get_itm(mtr, st, col=None):
    if col != None:
        return mtr[st][col]
    return mtr[st]




def main():
    n = int("Введите количество строк: ")
    m = int("Введите количество столбцов: ")
    mtr = [[-8, -14, -19, -18],
           [25, 28, 26, 20],
           [11, 18, 20, 25]]
    print(f"Температура на 2-й метеостанции за 4-й день: {get_itm(mtr, 1, 3)}")
    print(f"Температура на 3-й метеостанции за 1-й день: {get_itm(mtr, 2, 3)}")
    print(f"Показания термометров всех метеостанций за 2-й день: {[get_itm(mtr, i, 1) for i in range(n)]}")
    res = get_itm(mtr, 2)
    print(f"Среднюю температура на 3-й метеостанции: {sum(res) / len(res)}")

    for i in range(n):
        for ii in range(m):
            if 24 <= get_itm(mtr, i, ii) <= 26:
                print(f"На метеостанции {i + 1} в день {ii + 1} температура в диапазоне 24-26 градусов")

    

if __name__ == "__main__":
    main()