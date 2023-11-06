



import datetime


def main():
    '''Функция main'''
    date_now = str(datetime.date.today())
    date_now = date_now.split("-")
    print(f"Дата в формате дд.мм.гггг: {date_now[-1]}.{date_now[1]}.{date_now[0]}")
    
    
if __name__ == "__main__":
    main()