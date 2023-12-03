



def bubble_sort(arr):
    LEN = len(arr)
    
    for i in range(LEN):
        itr = LEN - i - 1
        flag = True
        for ii in range(itr):
            if arr[ii] > arr[ii + 1]:
                arr[ii + 1], arr[ii] = arr[ii], arr[ii + 1]
                flag = False
        if flag:
            break


def main():
    ls = []
    LEN = int(input("Введите длину массива: "))
    for i in range(LEN):
        ls.append(float(input("Введите значение элента: ")))
        
    bubble_sort(ls)
    print("Отсортированный массив:", ls)

if __name__ == "__main__":
    main()