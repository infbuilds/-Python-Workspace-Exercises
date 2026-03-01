import time

def time_calc(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            result = func(*args, **kwargs)
            end = time.time()
            
            print(f"function duration: {end - start} seconds")
            
            time.sleep(1) 
            return result
            
        except Exception as e:
            
            print(f"Error occurred: {e}")
            return None
            
    return wrapper

@time_calc
def get_squares(my_list):
    res = []
    for i in my_list:
        res.append(i**2)
    return res

@time_calc
def get_cubes(my_list):
    res = []
    for i in my_list:
        res.append(i**3)
    return res

@time_calc
def sum_all(*args):
    res = 0
    for i in args:
        time.sleep(1) 
        res += i
    return res

@time_calc
def multiply_all(*args):
    res = 1
    for i in args:
        res *= i
    return res

@time_calc
def divide_all(*args):
    res = args[0]
    for i in args[1:]:
        res /= i
    return res


print(get_squares("python"))


print(divide_all(10, 0))
