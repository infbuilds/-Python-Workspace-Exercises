import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"function duration: {end - start} seconds")
        time.sleep(1)
        return result
    return wrapper

@timer
def get_squares(list_data):
    res = []
    for i in list_data:
        res.append(i**2)
    return res

@timer
def get_cubes(list_data):
    res = []
    for i in list_data:
        res.append(i**3)
    return res

@timer
def sum_all(*args):
    res = 0
    for i in args:
        time.sleep(1) # senin eklediğin bekleme
        res += i
    return res

@timer
def multiply_all(*args):
    res = 1
    for i in args:
        res *= i
    return res

# Test
print(get_squares(range(1000)))
