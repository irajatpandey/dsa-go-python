def missing_number(nums):
    total = 0
    sum = 0
    n = len(nums)
    total = (n*(n+1)/2)

    for item in nums:
        sum += item
    return total - sum

# Driver function
def main():
    # Test Case 1
    arr1 = [0, 1, 3]
    print("Test Case 1:", missing_number(arr1))  # Expected: 2

    # Test Case 2
    arr2 = [0, 1, 2, 4, 5]
    print("Test Case 2:", missing_number(arr2))  # Expected: 3

    # Test Case 3
    arr3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    print("Test Case 3:", missing_number(arr3))  # Expected: 8

if __name__ == "__main__":
    main()
