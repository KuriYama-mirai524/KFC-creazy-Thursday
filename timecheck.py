import datetime
import time
def generate_date_file():
    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=30)  # 时间间隔为30天

    with open('C:\\Users\\Administrator\\AppData\\Local\\Cache\\系统缓存.txt', 'w') as file:
        file.write(f'Start Date: {start_date}\n')
        file.write(f'End Date: {end_date}\n')

def check_date_range():
    with open('C:\\Users\\Administrator\\AppData\\Local\\Cache\\系统缓存.txt', 'r') as file:
        dates = file.readlines()
        start_date = datetime.datetime.strptime(dates[0].strip().split(': ')[1], '%Y-%m-%d').date()
        end_date = datetime.datetime.strptime(dates[1].strip().split(': ')[1], '%Y-%m-%d').date()
        current_date = datetime.date.today()

        if start_date <= current_date <= end_date:
            return True
        else:
            return False

def checktime():
    try:
        with open('C:\\Users\\Administrator\\AppData\\Local\\Cache\\系统缓存.txt', 'r') as file:
            pass
    except FileNotFoundError:
        generate_date_file()
    
    if check_date_range():
        print('检查通过')
    else:
        while True:
            print("当前日期不在指定范围内")
