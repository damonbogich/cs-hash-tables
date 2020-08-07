# exps(x, y, z) =
#      if x <= 0: y + z
#      if x >  0: exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)


def exps(x, y, z):
    if x <= 0:
        return y+z
    else:
        return  exps(x-1,y+1,z) + exps(x-2,y+2,z*2) + exps(x-3,y+3,z*3)

print(exps(1,2,3))

