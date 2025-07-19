import time

print("Hello world")
print("Hi My Name is Nagesh")

def total_exe_time():
    print("Entered to the time function")
    start_time = time.time()
    time.sleep(15)
    end_time = time.time()
    print(f'Total Exception time is : {abs(end_time-start_time)}')
    print(f'Name of the function is : {__name__}')

if __name__ == '__main__':
    total_exe_time()