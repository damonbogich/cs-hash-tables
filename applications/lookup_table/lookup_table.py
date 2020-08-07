# Your code here
import math
import random

#cache results after x and y are run
# cache [x,y] = v

#cache the results of slowfun_to_slow
cache = {}
def slowfun_too_slow(x, y):
    
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653  # what is the point of this?  remainder is the number every time

    # cache[x,y] = v
    # return cache[x,y]
    return v


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    my_key = (x, y)
    if my_key in cache.keys():
        return cache[my_key]
    else:
        cache[my_key] = slowfun_too_slow(x,y)
        return cache[my_key]

    

    
    



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')


# cache = {}

# def fib(n):
#     # base case
#     if n <= 1:
#         return n

#     if n not in cache:
#         cache[n] = fib(n-1) + fib(n-2)

#     return cache[n]