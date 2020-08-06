
#recursive function that will take forever to calculate if inputs are big enough 
# want to store the results of (x,y,z) in cache so that the values will come up quickly

#want to store the results of the function in a tuple => (x,y,z)

#check in the function if the result of the function has been stored
    #if it has not we want to run the function and store the answer
    # if it has, we just want to return the answer from cache

cache = {}

def expensive_seq(x, y, z):
    my_key = (x, y, z)

    if my_key in cache.keys():
        return cache[my_key]
    else:
        if x <= 0:
            cache[my_key] = y+z
        else:
            cache[my_key] = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
        return cache[my_key]



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
