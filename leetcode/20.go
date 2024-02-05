package main

import "fmt"

var pattern = map[rune]rune{
	'(': ')',
	'[': ']',
	'{': '}',
}

func isValid(s string) bool {
	stack := make([]rune, 0)
	for _, c := range s {
		if val, ok := pattern[c]; ok {
			stack = append(stack, val)
		} else if len(stack) == 0 || stack[len(stack)-1] != c {
			return false
		} else {
			stack = stack[:len(stack)-1] // Correctly pop the element from the stack
		}

	}
	return len(stack) == 0
}

func main() {
	fmt.Println(isValid("()"))     // true
	fmt.Println(isValid("()[]{}")) // true
	fmt.Println(isValid("(]"))     // false
	fmt.Println(isValid("]"))      // false
}
