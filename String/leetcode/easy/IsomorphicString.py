# https://leetcode.com/problems/isomorphic-strings/
def isIsomorphic(s, t):
    map1 = {}
    map2 = {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        char1 = s[i]
        char2 = t[i]
        if char1 in map1:
            if map1[char1] != char2:
                return False
        else:
            if char2 in map2:
                return False
            else:
                map1[char1] = char2
                map2[char2] = True
    return True

# Example usage
if __name__ == "__main__":
    test_cases = [
        ("egg", "add"),
        ("foo", "bar"),
        ("paper", "title"),
    ]
    
    for i, (s, t) in enumerate(test_cases, 1):
        result = isIsomorphic(s, t)
        print(f"Test Case {i}: {result}")