#https://leetcode.com/problems/kth-missing-positive-number/    
def findKthPositive(arr, k):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        missing_count = arr[mid] - (mid + 1)
        
        if missing_count < k:
            start = mid + 1
        else:
            end = mid - 1
    return start + k

# Example usage
if __name__ == "__main__":
    test_cases = [
        ([2, 3, 4, 7, 11], 5),
        ([1, 2, 3, 4], 2),
        ([1, 3, 5, 6], 4)
    ]
    
    for i, (arr, k) in enumerate(test_cases, 1):
        result = findKthPositive(arr, k)
        print(f"Test Case {i}: The {k}th missing positive number is: {result}")