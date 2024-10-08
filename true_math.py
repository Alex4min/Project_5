from math import inf

def divide(first, second):
    if second != 0:
        del_2 = first / second
        return del_2
    else:
        return inf
print(divide(99 , 3))
print(divide(21, 0))