// https://leetcode.com/problems/two-sum/
package main

import "fmt"

func twoSum(nums []int, target int) []int {
    hashMap := make(map[int]int)
    result := []int{-1, -1}
	for i, num := range nums {
        if value, ok := hashMap[target-nums[i]]; ok {
            result[0] = value
            result[1] = i

            return result
        }

        hashMap[num] = i
    }
    return result

}

func twoSumMain() {
    testCases := []struct {
        nums   []int
        target int
    }{
        {[]int{2, 7, 11, 15}, 9},
        {[]int{3, 2, 4}, 6},
        {[]int{3, 3}, 6},
    }

    for i, testCase := range testCases {
        fmt.Printf("Test Case %d: %v\n", i+1, twoSum(testCase.nums, testCase.target))
    }
}

