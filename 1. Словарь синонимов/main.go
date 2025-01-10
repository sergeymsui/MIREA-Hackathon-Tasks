// Вам дан словарь, состоящий из пар слов.
// Каждое слово является синонимом к парному ему слову.
// Все слова в словаре различны. Для одного данного слова определите его синоним.

// Формат ввода
// Программа получает на вход количество пар синонимов N.
// Далее следует N строк, каждая строка содержит ровно два слова-синонима.
// После этого следует одно слово.

// Формат вывода
// Программа должна вывести синоним к данному слову.

// Примечание
// Эту задачу можно решить и без словарей (сохранив все входные
// данные в списке), но решение со словарем будет более простым.

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
