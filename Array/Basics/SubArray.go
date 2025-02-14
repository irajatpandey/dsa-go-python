package main

func printSubArray(arr []int) {
    for i := 0; i < len(arr); i++ {
        for j := i; j < len(arr); j++ {
            for k := i; k <= j; k++ {
                print(arr[k], " ")
            }
            println() // Print a new line after each subarray
        }
    }
}

func printSubArrayMain() {
	arr := []int{1, 2, 3, 4, 5}
	printSubArray(arr)

}