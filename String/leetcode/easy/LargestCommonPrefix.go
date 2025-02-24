// https://leetcode.com/problems/longest-common-prefix/description/
package main

import (
	"fmt"
	"sort"
	"strings"
)

// Solution struct
type Solution struct{}

// LongestCommonPrefix finds the longest common prefix among the list of strings
func (s *Solution) LongestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	// Sort the list lexicographically
	sortStrings(strs)

	// The first string is the smallest, and the last is the largest
	smallestString := strs[0]
	largestString := strs[len(strs)-1]

	// Initialize the common prefix
	var commonPrefix strings.Builder

	// Determine the minimum length to avoid index out of range
	minLength := min(len(smallestString), len(largestString))

	// Iterate through each character up to the minimum length
	for i := 0; i < minLength; i++ {
		if smallestString[i] == largestString[i] {
			commonPrefix.WriteByte(smallestString[i])
		} else {
			break
		}
	}

	return commonPrefix.String()
}

// Helper function to sort strings lexicographically
func sortStrings(strs []string) {
	sort.Strings(strs)
}

// Helper function to find the minimum of two integers
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// Driver function
func LongestCommonPrefixHelper() {
	solution := Solution{}

	// Test Case 1
	strs1 := []string{"flower", "flow", "flight"}
	fmt.Printf("Input: %v\nOutput: \"%s\"\n\n", strs1, solution.LongestCommonPrefix(strs1))

	// Test Case 2
	strs2 := []string{"dog", "racecar", "car"}
	fmt.Printf("Input: %v\nOutput: \"%s\"\n\n", strs2, solution.LongestCommonPrefix(strs2))

	// Test Case 3
	strs3 := []string{"interspecies", "interstellar", "interstate"}
	fmt.Printf("Input: %v\nOutput: \"%s\"\n\n", strs3, solution.LongestCommonPrefix(strs3))

	// Test Case 4
	strs4 := []string{"throne", "throne"}
	fmt.Printf("Input: %v\nOutput: \"%s\"\n\n", strs4, solution.LongestCommonPrefix(strs4))

	// Test Case 5
	strs5 := []string{}
	fmt.Printf("Input: %v\nOutput: \"%s\"\n\n", strs5, solution.LongestCommonPrefix(strs5))

	// Test Case 6
	strs6 := []string{"", "b"}
	fmt.Printf("Input: %v\nOutput: \"%s\"\n\n", strs6, solution.LongestCommonPrefix(strs6))
}