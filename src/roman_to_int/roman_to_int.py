# 1 - 3999
# 1 I
# 5 V
# X X
# 50 L
# 100 C
# 500 D
# 1000 M
# I, II, III, IIII, V, VI, VII, VIII, VIIII, X.
# X, XX, XXX, XL, L, LX, LXX, LXXX, XC, C.
# C, CC, CCC, CD, D, DC, DCC, DCCC, CM, M.


def romanToInt(s):
    return match_int(s, 0, 0)
    """
    :type s: str
    :rtype: int
    """


def match_int(s, i, num):
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
    temp = ''
    while x1 in s or x5 in s:
        temp = s[-1:] + temp
        s = s[:-1]
    if temp == x1:
        return match_int(s, i + 1, num + 1 * 10 ** i)
    elif temp == x1 + x1:
        return match_int(s, i + 1, num + 2 * 10 ** i)
    elif temp == x1 + x1 + x1:
        return match_int(s, i + 1, num + 3 * 10 ** i)
    elif temp == x1 + x5:
        return match_int(s, i + 1, num + 4 * 10 ** i)
    elif temp == x5:
        return match_int(s, i + 1, num + 5 * 10 ** i)
    elif temp == x5 + x1:
        return match_int(s, i + 1, num + 6 * 10 ** i)
    elif temp == x5 + x1 + x1:
        return match_int(s, i + 1, num + 7 * 10 ** i)
    elif temp == x5 + x1 + x1 + x1:
        return match_int(s, i + 1, num + 8 * 10 ** i)
    elif temp == x1 + x10:
        return match_int(s, i + 1, num + 9 * 10 ** i)
    if not s == '':
        return match_int(s, i + 1, num)
    return num


print(romanToInt('MCMLXXXIV'))  # 1984
print(romanToInt('MDCCLXXVI'))  # 1776
print(romanToInt('MCMLIV'))  # 1954
print(romanToInt('MCMXC'))  # 1990
print(romanToInt('MMXIV'))  # 2014
print(romanToInt('DCXXI'))  # 621
