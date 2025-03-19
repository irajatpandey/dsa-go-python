def numberOfSubstrings_brute_force(s):
    n = len(s)
    count = 0

    # Generate all substrings
    for i in range(n):
        found = {'a': 0, 'b': 0, 'c': 0}
        for j in range(i, n):
            found[s[j]] += 1

            # If substring contains 'a', 'b', 'c', count it
            if found['a'] > 0 and found['b'] > 0 and found['c'] > 0:
                count += 1

    return count

def numberOfSubstrings_optimized(s):
    left, ans = 0, 0
    freq = {'a': 0, 'b': 0, 'c': 0}

    for right in range(len(s)):
        freq[s[right]] += 1  # Expand the window

        # Shrink window until it contains at least one 'a', 'b', 'c'
        while all(freq[c] > 0 for c in 'abc'):
            ans += len(s) - right  # Count valid substrings
            freq[s[left]] -= 1
            left += 1  # Shrink window

    return ans

if __name__ == "__main__":
    s = "abcabc"
    
    print("Brute Force Output:", numberOfSubstrings_brute_force(s))
    print("Optimized Output:", numberOfSubstrings_optimized(s))
