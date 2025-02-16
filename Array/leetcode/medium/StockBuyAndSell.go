// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
package main

import "fmt"

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func maxProfit(prices []int) int {
    minPrice, maxProfit := int(^uint(0) >> 1), 0
	for _, price := range prices {
		minPrice = min(minPrice, price)
		maxProfit = max(maxProfit, price-minPrice)
	}
    return maxProfit
}

func maxProfitHelper() {
    testCases := [][]int{
        {7, 1, 5, 3, 6, 4},
        {7, 6, 4, 3, 1},
        {1, 2, 3, 4, 5},
    }

    for i, prices := range testCases {
        fmt.Printf("Test Case %d: %d\n", i+1, maxProfit(prices))
    }
	fmt.Println()
}
