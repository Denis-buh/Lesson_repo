



def fun(n):
    r1 = (-1) ** n
    r2 = 2 ** n
    return r1 / r2

def main():
    n = 1
    e = 0.0001
    pos_sum = 0
    while True:
        res = fun(n)
        if abs(res) < e:
            break
        pos_sum += res
        n += 1
    print(f"Сумма ряда {pos_sum}")
    
if __name__ == "__main__":
    main()