#https://leetcode.com/problems/single-number/
def single_number(arr, n):
    result = 0
    for value in arr:
        result ^= value
    return result        

arr1 = [1, 2, 1, 2, 4]
print("Test Case 1:", single_number(arr1, len(arr1)))

arr2 = [2, 2, 1]
print("Test Case 2:", single_number(arr2, len(arr2)))

arr3 = [4, 1, 2, 1, 2]
print("Test Case 3:", single_number(arr3, len(arr3)))
