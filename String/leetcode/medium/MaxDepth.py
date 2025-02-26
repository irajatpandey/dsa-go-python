#https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
def main():
    solution = Solution()  # Class ka object create karna hoga
    test_cases = [
        "((()))",    # Output: 3
        "(1+(2*3)+((8)/4))+1",  # Output: 3
        "(())()",    # Output: 2
        "",          # Output: 0
        "(()(())())" # Output: 3
    ]
    
    for s in test_cases:
        print(f"Input: {s} -> Max Depth: {solution.maxDepth(s)}")

# Class define karni hogi jisme maxDepth function ho
class Solution:
    def maxDepth(self, s):
        stack = []
        answer = 0
        for char in s:
            if char == '(':
                stack.append(char)
                answer = max(answer, len(stack))
            if char == ')':
                stack.pop()
        return answer

# Driver function ko call karna
if __name__ == "__main__":
    main()
