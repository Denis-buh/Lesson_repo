



def main():
    sp = []
    for i in range(12):
        sp.append(float(input("Введите значение числа: ")))
        
    print(f"Первоначальный список: {sp}")
    ind = sp.index(min(sp))
    sp[0], sp[ind] = sp[ind], sp[0]
    print(f"Измененый список: {sp}")
    
    
if __name__ == "__main__":
    main()
    
'''
Первоначальный список: [3456.0, 34.0, 5623.0, 456.0, 3456.0, 23456.0, 0.0, 3456.0, 3245.0, 234.0, 3.0, 43.0]
Измененый список: [0.0, 34.0, 5623.0, 456.0, 3456.0, 23456.0, 3456.0, 3456.0, 3245.0, 234.0, 3.0, 43.0]

'''
