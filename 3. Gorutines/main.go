package main

import (
	"fmt"
	"time"
)

func changeName(val *int) {
	*val = 20
}

func changeVal(g **int) {
	x := 20
	*g = &x
	fmt.Println("g = ", **g)
}

func add(arr []int, elem int) {
	arr = append(arr, elem)
	arr = append(arr, elem+1)
	arr[0] = 300
	fmt.Println(arr, len(arr), cap(arr))
}

func fixArr(arr [5]int) {
	arr[0] = 10
}

func show(arr [5]int) {
	for i := range 5 {
		fmt.Println(arr[i])
	}
}

type GlobalEnv int

const (
	None GlobalEnv = iota
	IntType
	FloatType
	BoolType
)

func main() {
	counter := 20

	for i := 0; i <= counter; i++ {

		go func() {
			fmt.Println(i * i)
		}()
	}

	time.Sleep(time.Second)
}
