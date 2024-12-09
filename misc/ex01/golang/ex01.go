package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"strings"
)

type nlp struct {
	n int
	l int
	p int
}

func check(e error) {
	if e != nil {
		log.Fatal(e)
		os.Exit(1)
	}
}

func getIndex(line, c string) (int, error) {
	idx := strings.Index(line, c)

	if idx > -1 {
		return idx, nil
	}
	return 0, errors.New("Invalid format")
}

func main() {
	argsWithProg := os.Args

	file_name := argsWithProg[1]
	file, err := os.Open(file_name)
	check(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	data := nlp{0, 0, 0}
	for scanner.Scan() {
		line := scanner.Text()

		n_idx, err := getIndex(line, "N")
		check(err)
		data.n += n_idx + 1
		l_idx, err := getIndex(line, "L")
		check(err)
		data.l += l_idx + 1
		p_idx, err := getIndex(line, "P")
		check(err)
		data.p += p_idx + 1
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(1*data.n + 2*data.l + 3*data.p)
}
