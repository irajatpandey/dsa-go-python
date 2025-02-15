package main

import "fmt"
func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

// longestSubArrayWithKSum finds the length of the longest subarray with sum equal to k.
func longestSubArrayWithKSum(arr []int, k int) int {
    prefixSumMap := make(map[int]int)
    maxLength := 0
    sum := 0
    for i := 0; i < len(arr); i++ {
        sum += arr[i]
        value, exists := prefixSumMap[sum - k]
        if exists {
            currentLength := i - value
            maxLength = max(maxLength, currentLength)
        }

        if _, exists := prefixSumMap[sum]; !exists {
            prefixSumMap[sum] = i
        }

    }

    return maxLength
}

func longestSubArrayWithKSumMain() {
    arr := []int{1, 2, 3, -3, 1, 1, 1, 4, 2, -3}
    k := 5
    result := longestSubArrayWithKSum(arr, k)
    fmt.Printf("Length of the longest subarray with sum %d is: %d\n", k, result)
}