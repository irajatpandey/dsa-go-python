#https://leetcode.com/problems/valid-anagram/
def isAnagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams of each other.

    Args:
        s (str): The first string.
        t (str): The second string.

    Returns:
        bool: True if s and t are anagrams, False otherwise.
    """
    # If lengths differ, they cannot be anagrams
    if len(s) != len(t):
        return False

    # Initialize a dictionary to store character counts
    map = {}

    # Count characters in string s
    for i in s:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    # Subtract character counts using string t
    for i in t:
        if i in map:
            map[i] -= 1
            # If count goes below zero, t has an extra character
            if map[i] < 0:
                return False
        else:
            # If character in t is not in s, not an anagram
            return False

    # Check if all counts are zero
    for item in map.values():
        if item != 0:
            return False

    return True


def driver():
    """
    Driver function to test the isAnagram function.
    """
    test_cases = [
        ("listen", "silent"),
        ("hello", "billion"),
        ("triangle", "integral"),
        ("", ""),
        ("a", "a"),
        ("abc", "cba"),
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("hello", "bello"),
        ("123", "321"),
        ("!@#", "#@!"),
        ("abc", "abcd"),
    ]

    for idx, (s, t) in enumerate(test_cases, 1):
        result = isAnagram(s, t)
        print(f"Test Case {idx}: isAnagram('{s}', '{t}') = {result}")


if __name__ == "__main__":
    driver()