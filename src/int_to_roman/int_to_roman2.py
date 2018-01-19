# 1-3999
# 1 I
# 5 V
# 10 X
# 50 L
# 100 C
# 500 D
# 1000 M
# I, II, III, IV, V, VI, VII, VIII, IX, X.
# X, XX, XXX, XL, L, LX, LXX, LXXX, XC, C.
# C, CC, CCC, CD, D, DC, DCC, DCCC, CM, M.
def intToRoman(num):
    return match_roman(num, 0, '')


def match_roman(num, i, s):
    x1 = 'I'
    x5 = 'V'
    x10 = 'X'
    if i == 1:
        x1 = 'X'
        x5 = 'L'
        x10 = 'C'
    elif i == 2:
        x1 = 'C'
        x5 = 'D'
        x10 = 'M'
    elif i == 3:
        x1 = 'M'
    temp = num % 10
    num = int(num / 10)
    if num == 0:
        if temp < 4:
            return x1 * temp + s
        elif temp == 4:
            return x1 + x5 + s
        elif temp == 5:
            return x5 + s
        elif temp == 6:
            return x5 + x1 + s
        elif temp < 9:
            return x5 + x1 * (temp - 5) + s
        elif temp == 9:
            return x1 + x10 + s
        else:
            return x10 + s
    else:
        if temp < 4:
            return match_roman(num, i + 1, x1 * temp + s)
        elif temp == 4:
            return match_roman(num, i + 1, x1 + x5 + s)
        elif temp == 5:
            return match_roman(num, i + 1, x5 + s)
        elif temp == 6:
            return match_roman(num, i + 1, x5 + x1 + s)
        elif temp < 9:
            return match_roman(num, i + 1, x5 + x1 * (temp - 5) + s)
        elif temp == 9:
            return match_roman(num, i + 1, x1 + x10 + s)
        else:
            return match_roman(num, i + 1, x10 + s)


e1 = 1
e2 = 8
e3 = 28
e4 = 59
e5 = 123
e6 = 1990
e7 = 3854
e8 = 1776
e9 = 1954
e10 = 1990
e11 = 2014
print(intToRoman(e1))
print(intToRoman(e2))
print(intToRoman(e3))
print(intToRoman(e4))
print(intToRoman(e5))
print(intToRoman(e6))
print(intToRoman(e7))
print(intToRoman(e8))
print(intToRoman(e9))
print(intToRoman(e10))
print(intToRoman(e11))