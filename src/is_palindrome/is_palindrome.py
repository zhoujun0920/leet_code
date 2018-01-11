def is_palindrome(x):
    s = str(x)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i = i + 1
        j = j - 1
    return True


e1 = 1
e2 = 121
e3 = 123321
e4 = 1234
e5 = -2147447412

print(is_palindrome(e1))
print(is_palindrome(e2))
print(is_palindrome(e3))
print(is_palindrome(e4))
print(is_palindrome(e5))
