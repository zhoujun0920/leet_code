def is_match(s, p):
    if s is '':
        if p is '':
            return True
        elif len(p) > 1:
            if p[-1] == '*':
                return is_match(s, p[:-2])
            return False
        elif p[-1] == '.':
            return True
        return False
    if p is '':
        if s is '':
            return True
        elif len(s) > 1:
            if s[-1] == '*':
                return is_match(s[:-2], p)
            return False
        elif s[-1] == '.':
            return True
        return False
    if s[-1] == p[-1] or s[-1] == '.' or p[-1] == '.':
        return is_match(s[:-1], p[:-1])
    if len(s) > 1 or len(p) > 1:
        if len(s) > 1:
            if s[-1] == '*':
                if s[-2] == p[-1] or s[-2] == '.':
                    return is_match(s, p[:-1])
                return is_match(s[:-2], p)
        if len(p) > 1:
            if p[-1] == '*':
                if p[-2] == s[-1] or p[-2] == '.':
                    return is_match(s[:-1], p)
                return is_match(s, p[:-2])
        return False
    return False


# print(is_match("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))  # -> false
print(is_match("aaa", "ab*a*c*a"))  # → true
# print(is_match("a", ".*..a*"))  # -> false
# print(is_match("a", "ab*a"))  # -> false
# print(is_match("ab", ".*c"))  # -> false
# print(is_match("aa", "a"))  # → false
# print(is_match("aaa", "aa"))  # → false
# print(is_match("ab", ".*c"))  # → false
# print(is_match("aa", "a"))  # → false
# print(is_match("aaa", "aa"))  # → false
# print('--------------------------------')
# print(is_match("bbbba", ".*a*a"))  # -> true
# print(is_match("aaa", "a*a"))  # -> true
# print(is_match("aa", "aa"))  # → true
# print(is_match("aa", "a*"))  # → true
# print(is_match("aa", ".*"))  # → true
# print(is_match("ab", ".*"))  # → true
# print(is_match("aab", "c*a*b"))  # → true
# print(is_match("a", "ab*"))  # → true
# print(is_match("aaa", "ab*ac*a"))  # → true
# print(is_match("aa", "aa"))  # → true
# print(is_match("aa", "a*"))  # → true
# print(is_match("aa", ".*"))  # → true
# print(is_match("ab", ".*"))  # → true
# print(is_match("aab", "c*a*b"))  # → true
# print(is_match("ab", ".*..c*"))  # → true