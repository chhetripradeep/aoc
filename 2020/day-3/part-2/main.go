package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

func readInput(filepath string) [][]string {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	input := make([][]string, 0)
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		characters := strings.Split(line, "")
		input = append(input, characters)
	}
	return input
}

func calculate(input [][]string, right int, down int) int {
	width := len(input[0])
	height := len(input)
	x, y := 0, 0
	count := 0
	for x < height {
		if y > width - 1 {
			y = y - width
		}
		if input[x][y] == string('#') {
			count += 1
		}
		x = x + down
		y = y + right
	}
	return count
}

func main() {
	right_downs := [][]int{
		{1, 1},
		{3, 1},
		{5, 1},
		{7, 1},
		{1, 2},
	}
	input := readInput("input.txt")
	result := 1
	for i := range right_downs {
		result = result * calculate(input, right_downs[i][0], right_downs[i][1])
	}
	fmt.Println(result)
}
