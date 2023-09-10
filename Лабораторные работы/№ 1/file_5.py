



nimber_month = int(input("Введите номер месяца: "))

if nimber_month > 12 or nimber_month < 1:
    print("Введено не верное значение")

if nimber_month == 2:
    print("Количество дней в месяце = 28")

elif (nimber_month == 4 or nimber_month == 6 or 
      nimber_month == 9 or nimber_month == 11):
    print("Количество дней в месяце = 30")

else:
    print("Количество дней в месяце = 31")