package main

import "fmt"

func findMaxConsecutiveOnes(arr []int) int {
	maxCount := 0
	ans := 0
	for i := 0; i < len(arr); i++ {
		if arr[i] == 1 {
			maxCount++
		} else {
			ans = max(ans, maxCount)
			maxCount = 0
		}
	}
	ans = max(ans, maxCount)
	return ans
}
func findMaxConsecutiveOnesMain() {
	arr := []int{1, 1, 0, 1, 1, 1}
	fmt.Println(findMaxConsecutiveOnes(arr)) // Output: 3
}
