def longest_subarray_with_k_sum(arr, k):
     maxLength = 0
     sum = 0
     prefixSumMap = {}
     
     
     for i in range(len(arr)):
         sum += arr[i]
         if (sum - k) in prefixSumMap:
             maxLength = max(maxLength, i - prefixSumMap[sum - k])
     
         if sum not in prefixSumMap:
             prefixSumMap[sum] = i
     
     return maxLength

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
    k = 5
    result = longest_subarray_with_k_sum(arr, k)
    print(f"Length of the longest subarray with sum {k} is: {result}")