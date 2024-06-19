package main

import "fmt"

func main() {
	// Creating a 2D array
	arr2D := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}

	// Accessing elements
	fmt.Println(arr2D[0][1]) // Output: 2
	fmt.Println(arr2D[2][2]) // Output: 9

	// Traversing a 2D array
	for _, row := range arr2D {
		for _, elem := range row {
			fmt.Print(elem, " ")
		}
	}
	// Output: 1 2 3 4 5 6 7 8 9
}
