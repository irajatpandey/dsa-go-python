# https://leetcode.com/problems/largest-odd-number-in-string/

def largest_odd_number(num):
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[:i + 1]
    return ""

# Example usage
if __name__ == "__main__":
    test_cases = [
        "52",
        "4206",
        "35427"
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        result = largest_odd_number(test_case)
        print(f"Test Case {i}: {result}")
    