
# pythran export capsule add_int(int, int)
def add_int(f, g):
    return f + g

# pythran export capsule add(float[][], float[][])
def add(f, g):
    return f + g

# pythran export add2_int(int, int, int(int, int))
def add2_int(f, g, add_func):
    return add_func(f, g)

# pythran export add2(float[][], float[][], float[][](float[][], float[][]))
def add2(f, g, add_func):
    return add_func(f, g)