def length_of_longest_substring(s):
    longest_substring = ''
    temp_substring = ''
    for sub in list(s):
        if sub not in temp_substring:
            temp_substring = temp_substring + sub
            if len(temp_substring) > len(longest_substring):
                longest_substring = temp_substring
        else:
            temp_substring = temp_substring[temp_substring.index(sub) + 1:]
            temp_substring = temp_substring + sub
    return len(longest_substring)


e0 = 'c'  # c
e11 = 'au'  #au
e1 = 'abcabcbb'  # abc
e2 = 'bbbbb'  # b
e3 = 'pwwkew'  # wke
e4 = 'pwesvwk'  # pwesv
e5 = 'bpfbhmipx'  # fbhmipx


print(length_of_longest_substring(e0))
print(length_of_longest_substring(e11))
print(length_of_longest_substring(e1))
print(length_of_longest_substring(e2))
print(length_of_longest_substring(e3))
print(length_of_longest_substring(e4))
print(length_of_longest_substring(e5))