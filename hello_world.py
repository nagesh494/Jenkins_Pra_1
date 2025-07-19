import time
from datetime import date

print("Hello world")
print("Hi My Name is Nagesh")
print(date.today())

def print_date():
    print("Entered to the function")
    mt_time = date.today()
    print(f'Today date is : {mt_time}')

if __name__ == '__main__':
    print_date()