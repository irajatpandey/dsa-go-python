def sort_colors(nums):
    i = 0
    j = 0
    k = len(nums) - 1
    while j <= k:
        if nums[j] == 2:
            nums[j], nums[k] = nums[k], nums[j]
            k -= 1
        elif nums[j] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        else :
            j += 1

    

test_cases = [
    [2, 0, 2, 1, 1, 0],
    [2, 0, 1],
    [0],
    [1],
]

for i, nums in enumerate(test_cases, 1):
    sort_colors(nums)
    print(f"Test Case {i}:", nums)
