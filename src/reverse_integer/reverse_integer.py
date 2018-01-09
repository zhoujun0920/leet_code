def reverse_integer(x):
    is_negative = False
    if x < 0:
        is_negative = True
        x = -x
    x_string = str(x)
    x_string_reverse = x_string[::-1]
    temp = int(x_string_reverse)
    try:
        if is_negative:
            if not (int(temp) >> 31):
                return -temp
        if not (int(temp) >> 31):
            return temp
    except ValueError:
        return 0
    return 0


e1 = 123
e2 = -123
e3 = 120
e4 = 1563847412
print(reverse_integer(e1))
print(reverse_integer(e2))
print(reverse_integer(e3))
print(reverse_integer(e4))