package main

import "fmt"

func bubbleSort(arr []int) {
	for i := 0; i < len(arr); i++ {
		for j := 0; j < len(arr) - 1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
			}
		}
	}

	for _, value := range arr {
		fmt.Print(value, " ")
	}
}

func bubbleSortMain() {
	arr := []int{2, 1, 3, 5, 4}
	bubbleSort(arr)
}