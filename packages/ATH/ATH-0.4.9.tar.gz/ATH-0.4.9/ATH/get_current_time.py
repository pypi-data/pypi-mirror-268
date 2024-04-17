import datetime

def get_current_time():
    current_time = datetime.datetime.now()
    return current_time.strftime("%H:%M:%S")

def get_current_date():
    current_date = datetime.date.today()
    return current_date.strftime("%Y-%m-%d")

def get_current_date_and_time():
    time = get_current_time()
    date = get_current_date()
    return time, date