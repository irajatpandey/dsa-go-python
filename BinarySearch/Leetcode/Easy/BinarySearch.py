def binary_search(arr, target):
	start = 0
	end = len(arr) - 1

	while start <= end:
		mid = start + (end - start) // 2
		if arr[mid] == target:
			return mid
		elif arr[mid] > target:
			 end = mid - 1
		else:
			start = mid + 1
	return -1

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    target = 40
    result = binary_search(arr, target)
    print(f"Target {target} found at index: {result}")