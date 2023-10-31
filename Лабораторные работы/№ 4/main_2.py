



def main():
    sp = []
    for i in range(15):
        sp.append(float(input("Введите значение числа: ")))
        
    print(f"Максимальный элемент: {max(sp)}")
    print(f"Номер максимального элемента: {sp.index(max(sp)) + 1}")
    
    
if __name__ == "__main__":
    main()
    
