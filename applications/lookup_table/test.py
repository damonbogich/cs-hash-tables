import math
v = 19
print(v % 982451653)

# def slowfun_too_slow(x, y):
#     v = math.pow(x, y) #8
#     v = math.factorial(v) #8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40,320
#     v //= (x + y) #40,320 // 5 = 8,064
#     v %= 982451653

#     return v
# print(slowfun_too_slow(2,3))


cache = {}
# def slowfun_too_slow(x, y):
#     v = math.pow(x, y)
#     v = math.factorial(v)
#     v //= (x + y)
#     v %= 982451653  # what is the point of this?  remainder is the number every time

#     cache[x,y] = v
#     return v

# slowfun_too_slow(2,3)
# print(cache)
cache[2,3] = 45,000
print(cache)
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    if not cache[x,y]:
        return cache[x,y]
    else:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        cache[x,y] = v
        return v
    
slowfun(2,3)

cache2 = {}
cache2[(2,3)] = 14
my_key = (2, 3)
print(cache2)

if my_key in cache2.keys():
    print('true')
else:
    print('false')

