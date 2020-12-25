package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func readInput(filename string) ([]string, []string) {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	policies := make([]string, 0)
	passwords := make([]string, 0)
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := strings.Split(scanner.Text(), ":")
		policy, password := line[0], line[1]
		policies = append(policies, policy)
		passwords = append(passwords, password)
	}
	return policies, passwords
}

func isValid(policy string, password string) bool {
	p := strings.Split(policy, " ")
	count, character := p[0], p[1]
	c := strings.Split(count, "-")

	pos1, err := strconv.ParseInt(c[0],10 , 64)
	if err != nil {
		log.Fatal(err)
	}
	pos2, err := strconv.ParseInt(c[1], 10, 64)
	if err != nil {
		log.Fatal(err)
	}

	pass := strings.Split(password, "")
	if pass[pos1] == character && pass[pos2] != character {
		return true
	} else if pass[pos1] != character && pass[pos2] == character {
		return true
	} else {
		return false
	}
}

func calculate(policies []string, passwords []string) int {
	valid_passwords := 0
	for i, _ := range policies {
		if isValid(policies[i], passwords[i]) {
			valid_passwords += 1
		}
	}
	return valid_passwords
}

func main() {
	policies, passwords := readInput("input.txt")
	result:= calculate(policies, passwords)
	fmt.Println(result)
}
