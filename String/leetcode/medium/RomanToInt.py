#https://leetcode.com/problems/roman-to-integer/description/
def main():
    solution = Solution()  # Class ka object create karna hoga
    test_cases = [
        "III",      # Expected Output: 3
        "IV",       # Expected Output: 4
        "IX",       # Expected Output: 9
        "LVIII",    # Expected Output: 58
        "MCMXCIV"   # Expected Output: 1994
    ]
    
    for roman in test_cases:
        print(f"Input: {roman} -> Output: {solution.romanToInt(roman)}")


class Solution:
    def romanToInt(self, s):
        roman_map = {'I' : 1, 'V': 5, 'X' : 10, 'L' : 50, 'C' : 100, 'M' : 1000}
        ans = 0
        previous = None
        for char in s:
            if previous == None:
              ans += roman_map[char]
            else:
                if roman_map[char] > roman_map[previous]:
                    ans += roman_map[char] - 2 *roman_map[previous]
                else:
                    ans += roman_map[char]
            previous = char
        return ans

# Driver function ko call karna
if __name__ == "__main__":
    main()
