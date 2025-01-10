package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	n := 0
	fmt.Scan(&n)

	dict := []string{}
	synonym := []string{}

	scanner := bufio.NewScanner(os.Stdin)

	for i := 0; i < n; i++ {
		scanner.Scan()
		input := strings.Split(scanner.Text(), " ")

		dict = append(dict, input[0])
		synonym = append(synonym, input[1])
	}

	scanner.Scan()
	word := scanner.Text()

	for i := 0; i < n; i++ {
		if word == dict[i] {
			fmt.Println(synonym[i])
		} else if word == synonym[i] {
			fmt.Println(dict[i])
		}
	}
}
