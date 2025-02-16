#https://leetcode.com/problems/move-zeroes/description/

def move_zeroes(nums):
     i = 0
     for j in range(len(nums)):
        if nums[j] != 0:
           nums[i], nums[j] = nums[j], nums[i]
           i += 1

if __name__ == "__main__":
    # Test Case 1
    arr1 = [0, 1, 0, 3, 12]
    move_zeroes(arr1)
    print("Test Case 1:", arr1)  # Expected output: [1, 3, 12, 0, 0]

    # Test Case 2
    arr2 = [0, 0, 0, 1, 0]
    move_zeroes(arr2)
    print("Test Case 2:", arr2)  # Expected output: [1, 0, 0, 0, 0]

    # Test Case 3
    arr3 = [1, 2, 3, 4, 5]
    move_zeroes(arr3)
    print("Test Case 3:", arr3)  # Expected output: [1, 2, 3, 4, 5]
