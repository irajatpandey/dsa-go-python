def find_max_consecutive_ones(arr):
    max_count = 0
    ans = 0
    
    for num in arr:
        if num == 1:
            max_count += 1
        else:
            ans = max(ans, max_count)
            max_count = 0

    ans = max(ans, max_count)
    return ans

# Driver function
def find_max_consecutive_ones_main():
    arr = [1, 1, 0, 1, 1, 1]
    print(find_max_consecutive_ones(arr))  # Output: 3

find_max_consecutive_ones_main()
