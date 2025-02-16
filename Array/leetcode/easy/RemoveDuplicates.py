#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
def remove_duplicates(nums, n):
    i = 0
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            nums[i + 1] = nums[j]
            i += 1
    return i + 1

arr1 = [1, 2, 2, 2, 3, 3, 4]
output1 = remove_duplicates(arr1, len(arr1))
print("Test Case 1: New length =", output1)

arr2 = [1, 1, 2, 2, 3, 3, 3]
output2 = remove_duplicates(arr2, len(arr2))
print("Test Case 2: New length =", output2)

arr3 = [1, 1, 1, 1, 1]
output3 = remove_duplicates(arr3, len(arr3))
print("Test Case 3: New length =", output3)
