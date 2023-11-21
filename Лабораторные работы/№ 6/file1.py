



def main():
    '''Функция main'''
    s = input('Введите строку с выражением: ') 
    l = list(s)
    l += ["endl"]
    
    res = []
    ls_command = ("+", "-", "endl")
    number_op = ""

    for i in l:
        if i in ls_command:
            res.append(int(number_op))
            if i == "endl":
                res = sum(res)
            elif i == "+":
                number_op = ""
            elif i == "-":
                number_op = "-"
                 
        else:
            number_op += i
    print(f"Результат: {res}") 


if __name__ == "__main__":
    main()