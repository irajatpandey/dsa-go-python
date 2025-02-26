#https://leetcode.com/problems/string-to-integer-atoi/
class Solution(object):
    def my_strip(self, s, chars=" \t\n\r"):
        # Left side se characters hatane ke liye
        start = 0
        while start < len(s) and s[start] in chars:
            start += 1

        # Right side se characters hatane ke liye
        end = len(s) - 1
        while end >= 0 and s[end] in chars:
            end -= 1

        # Substring return karna (agar saara string strip ho gaya toh empty return hoga)
        return s[start:end + 1] if start <= end else ""

    def myAtoi(self, s):
        # Remove leading and trailing spaces
        s = self.my_strip(s)
        
        # ✅ Edge Case: Empty string
        if not s:
            return 0  

        # Initialize variables
        negative = False
        index = 0
        result = 0
        
        # ✅ Check sign
        if s[0] == '-':
            negative = True
            index += 1
        elif s[0] == '+':
            index += 1
        
        # ✅ Process numeric characters
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        # ✅ Apply sign
        if negative:
            result = -result
        
        # ✅ Handle integer limits (32-bit signed int)
        INT_MAX = 2**31 - 1  # 2147483647
        INT_MIN = -2**31     # -2147483648
        
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        "42",
        "   -42",
        "4193 with words",
        "words and 987",
        "-91283472332"
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        result = solution.myAtoi(test_case)
        print(f"Test Case {i}: {result}")