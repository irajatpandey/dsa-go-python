package main

import "fmt"

func arrayExample() {
    fmt.Println("Hello World")
	// Array Declaration
	var arr [5]int
	// Array Initialization
	arr[0] = 1
	arr[1] = 2
	arr[2] = 3
	arr[3] = 4
	arr[4] = 5

	// Array Declaration and Initialization
	arr1 := [5]int{1, 2, 3, 4, 5}

	// Print Array with Loop
	for i := 0; i < len(arr); i++ {
		fmt.Println(arr[i])
	}

	// Print Array with Range
	for i, v := range arr1 {
		fmt.Println(i, v)
	}
}