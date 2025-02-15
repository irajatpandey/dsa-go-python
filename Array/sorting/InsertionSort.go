package main

import "fmt"

func insertionSort(arr []int) {
	for i := 1; i < len(arr); i++ {
		key := arr[i]
		j := i - 1

		// Shift elements to the right until the correct position for key is found
		for j >= 0 && arr[j] > key {
			arr[j+1] = arr[j]
			j--
		}

		arr[j+1] = key
	}

	// Print the sorted array
	for _, value := range arr {
		fmt.Print(value, " ")
	}
	fmt.Println()
}

func insertionSortMain() {
	arr := []int{64, 34, 25, 12, 22, 11, 90}
	insertionSort(arr)
}
