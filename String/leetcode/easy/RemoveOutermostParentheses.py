def remove_outer_parentheses(s):
    ans = []
    counter = 0
    for bracket in s:
        if bracket == '(':
            if counter > 0:  # Only add '(' if it's not the outermost
                ans.append(bracket)
            counter += 1
        elif bracket == ')':
            counter -= 1
            if counter > 0:  # Only add ')' if it's not the outermost
                ans.append(bracket)
    return ''.join(ans)

      


# Example usage
if __name__ == "__main__":
    test_cases = [
        "(()())(())",
        "(()())(())(()(()))",
        "()()"
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        result = remove_outer_parentheses(test_case)
        print(f"Test Case {i}: {result}")