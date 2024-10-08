def divide(first, second):
    if second != 0:
        del_1 = first / second
        return del_1
    else:
        return 'Ошибка'
print(divide(69, 3))
print(divide(15,0))