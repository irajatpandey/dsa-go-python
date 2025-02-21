// https://leetcode.com/problems/largest-odd-number-in-string/

package main

import "fmt"

func largestOddNumber(num string) string {
    for i := len(num) - 1; i >= 0; i-- {
		if (num[i] - '0') % 2 != 0 {
			return num[:i+1]
		}
	}
    return ""
}

func largestOddNumberHelper() {
    testCases := []string{
        "52",
        "4206",
        "35427",
    }

    for i, testCase := range testCases {
        result := largestOddNumber(testCase)
        fmt.Printf("Test Case %d: %s\n", i+1, result)
    }
	fmt.Println()
}