# Implement your function below.

def is_one_away_same_length(s1, s2):
    n = len(s1)
    count = 0
    for i in range(n):
        if s1[i] != s2[i]:
            count += 1
            if count > 1:
                return False
    return True

def is_one_away_diff_lengths(s1, s2, n, m):
    count_diff = 0
    i = 0
    while i < m:
        if s2[i] == s1[i+count_diff]:
            i += 1
        else:
            count_diff += 1
            if count_diff > 1:
                return False
    return True
    
def is_one_away(s1, s2):
    n, m = len(s1), len(s2)
    if abs(n-m) > 1:
        return False
        
    if n == m:
        return is_one_away_same_length(s1, s2)
    elif n > m:
        return is_one_away_diff_lengths(s1, s2, n, m)
    else:
        return is_one_away_diff_lengths(s2, s1, m, n)
    


# NOTE: The following input values will be used for testing your solution.
assert is_one_away("abcde", "abcd") == True # should return True
assert is_one_away("abde", "abcde") == True # should return True
assert is_one_away("a", "a")  == True # should return True
assert is_one_away("abcdef", "abqdef") == True # should return True
assert is_one_away("abcdef", "abccef") == True # should return True
assert is_one_away("abcdef", "abcde") == True # should return True
assert is_one_away("aaa", "abc")  == False # should return False
assert is_one_away("abcde", "abc")  == False # should return False
assert is_one_away("abc", "abcde") == False # should return False
assert is_one_away("abc", "bcc") == False # should return False
