package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Node struct {
	val        int
	leftChild  *Node
	rightChild *Node
}

func NewNode(v int, l, r *Node) *Node {
	return &Node{
		val:        v,
		leftChild:  l,
		rightChild: r,
	}
}

func BuildTree(root *Node, v int) *Node {
	if root == nil {
		return NewNode(v, nil, nil)
	}
	if v < root.val {
		root.leftChild = BuildTree(root.leftChild, v)
	} else if v > root.val {
		root.rightChild = BuildTree(root.rightChild, v)
	}
	return root
}

func GetHeight(root *Node) int {
	if root == nil {
		return 0
	}
	return 1 + max(GetHeight(root.leftChild), GetHeight(root.rightChild))
}

func main() {
	var root *Node
	root = nil

	MaxBufferSize := 1024 * 1024
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer(make([]byte, MaxBufferSize), MaxBufferSize)
	scanner.Scan()

	input := strings.Split(scanner.Text(), " ")
	for _, e := range input {
		d, _ := strconv.Atoi(string(e))

		if d == 0 {
			break
		}

		root = BuildTree(root, d)
	}

	fmt.Println(GetHeight(root))
}
