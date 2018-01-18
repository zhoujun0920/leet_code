def is_match(s, p):
    if len(s) <= 1 and len(p) <= 1:
        if s is '':
            if p is '' or p[0] == '*' or p[0] == '.':
                return True
            return False
        if p is '':
            if s is '' or s[0] == '*' or s[0] == '.':
                return True
            return False
    if len(s) > 0 and len(p) > 0 and (s[0] == p[0] or s[0] == '.' or p[0] == '.'):
        if len(s) > 1 and len(p) > 1:
            if s[1] == '*':
                if p[0] == p[1]:
                    return is_match(s, p[1:])
                else:
                    if s[0] == '.':
                        return is_match(s[2:], '')
                    return is_match(s[2:], p[1:])
            if p[1] == '*':
                if s[0] == s[1]:
                    return is_match(s[1:], p)
                else:
                    if p[0] == '.':
                        return is_match('', p[2:])
                    return is_match(s[1:], p[2:])
        if len(s) > 1 and len(p) == 1:
            if (s[1] == '*' or s[0]) and s[0] == p[0]:
                return is_match(s[2:], p)
        if len(p) > 1 and len(s) == 1:
            if p[1] == '*' and s[0] == p[0]:
                return is_match(s, p[2:])
        return is_match(s[1:], p[1:])
    if len(s) > 1 or len(p) > 1:
        if len(s) > 1:
            if s[1] == '*':
                return is_match(s[2:], p)
        if len(p) > 1:
            if p[1] == '*':
                return is_match(s, p[2:])
        return False
    """
    :type s: str
    :type p: str
    :rtype: bool
    """

# print(is_match("aaa", "a*a"))  # -> true
# print(is_match("ab", ".*c"))  # -> false
# print(is_match("aa", "a"))  # → false
# print(is_match("aa", "aa"))  # → true
# print(is_match("aaa", "aa"))  # → false
print(is_match("aa", "a*"))  # → true
print(is_match("aa", ".*"))  # → true
print(is_match("ab", ".*"))  # → true
print(is_match("aab", "c*a*b"))  # → true
