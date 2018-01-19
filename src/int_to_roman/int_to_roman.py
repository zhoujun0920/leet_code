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
    i = 0
    s = ''
    while not num % 10 == 0 or num > 0:
        s = matchRoman(i, int(num % 10)) + s
        i = i + 1
        num = num / 10
    return s


def matchRoman(i, n):
    x1 = 'I'
    x5 = 'V'
    x10 = 'X'
    if i == 1:
        x1 = 'X'
        x5 = 'L'
        x10 = 'C'
    if i == 2:
        x1 = 'C'
        x5 = 'D'
        x10 = 'M'
    if i == 3:
        x1 = 'M'
    if n < 4:
        return x1 * n
    elif n == 4:
        return x1 + x5
    elif n == 5:
        return x5
    elif n == 6:
        return x5 + x1
    elif n < 9:
        return x5 + x1 * (n - 5)
    elif n == 9:
        return x1 + x10
    else:
        return x10


e1 = 10
e2 = 3
e3 = 8
e4 = 21
e5 = 38
e6 = 1776  # MDCCLXXVI
e7 = 1954  # MCMLIV
e8 = 1990  # MCMXC
e9 = 2014  # MMXIV
e10 = 3999  # MMMCMXCIX

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
