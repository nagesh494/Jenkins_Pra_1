import time
from datetime import date

print("Hello world")
print("Hi My Name is Nagesh")
print(date.today())

def print_date():
    print("Entered to the function")
    mt_time = date.today()
    print(f'Today date is : {mt_time}')

def total_exe_time():
    print("Entered to the time function")
    start_time = time.time()
    time.sleep(15)
    end_time = time.time()
    print(f'Total Exception time is : {abs(end_time-start_time)}')
    print(f'Name of the function is : {__name__}')

if __name__ == '__main__':
    total_exe_time()
    print_date()
