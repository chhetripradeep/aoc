package main

import (
	"bufio"
	"errors"
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

func calculate(input []int) (int, error) {
	length := len(input)
	for i := 0; i < length; i++ {
		for j := i; j < length; j++ {
			if input[i] + input[j] == 2020 {
				return input[i] * input[j], nil
			}
		}
	}
	return -1, errors.New("combination not found")
}

func main() {
	input := readInput("input.txt")
	result, err := calculate(input)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(result)
}
