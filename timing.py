import time

def calculate_time(func):
    def wrapper():
        current_time = time.time()
        func()
        print("Total time ", time.time() - current_time)

    return wrapper

@calculate_time
def aFunction():
    time.sleep(2)
    return;

def main():
    aFunction()
