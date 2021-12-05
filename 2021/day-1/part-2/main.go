package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func readInput(filename string) []int {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	input := make([]int, 0)
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		num, err := strconv.ParseInt(scanner.Text(), 10, 64)
		if err != nil {
			log.Fatal(err)
		}
		input = append(input, int(num))
	}

	if err = scanner.Err(); err != nil {
		log.Fatal(err)
	}
	return input
}

func sum(slice []int) int {
	result := 0
	for _, v := range slice {
		result += v
	}
	return result
}

func calculate(input []int) int {
	result := 0
	for i := 0; i < len(input)-3; i++ {
		if sum(input[i:i+3]) < sum(input[i+1:i+4]) {
			result += 1
		}
	}
	return result
}

func main() {
	input := readInput("input.txt")
	result := calculate(input)
	fmt.Println(result)
}
