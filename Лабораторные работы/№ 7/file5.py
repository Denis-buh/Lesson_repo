



import random


def quick_sort(arr:list, index:int=0) -> list:
    LEN = len(arr)
    if index == LEN:
        return arr

    X = arr[index] # Элемент по которому будем сортировать
    left_arr = []
    right_arr = []
    for i in arr:
        if X >= i:
            left_arr.append(i)
        elif X < i:
            right_arr.append(i)
    arr = left_arr + right_arr
    return quick_sort(arr, index + 1)

    


def main():
    '''Функция main'''
    ls = []
    LEN = int(input("Введите длину массива: "))
    for i in range(LEN):
        ls.append(float(input("Введите значение элента: ")))
    
    print(f"Массив до сортировки: {ls}")
    print(f"Массив после сортировки: {quick_sort(ls) }")


if __name__ == "__main__":
    main()