package main

import (
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

func main() {
	// 1. Basic String Declaration and Printing
	myStr := "Hello World"
	fmt.Println(myStr) // Output: Hello World

	// 2. Accessing Characters in a String
	fmt.Println(string(myStr[0])) // H
	fmt.Println(string(myStr[1])) // e
	fmt.Println(string(myStr[len(myStr)-1])) // d

	// 3. String Concatenation
	str1 := "Hello"
	str2 := "World"
	fmt.Println(str1 + " " + str2) // Hello World

	// 4. String Repetition (Using a loop since Go doesn't have a direct string repetition operator)
	fmt.Println(strings.Repeat(str1, 3)) // HelloHelloHello
	fmt.Println(strings.Repeat(str2, 2)) // WorldWorld

	// 5. Slice a String
	fmt.Println(myStr[0:5]) // Hello
	fmt.Println(myStr[6:])  // World
	fmt.Printf("%T\n", myStr[0:3]) // string

	// 6. String Length
	fmt.Println(len(myStr)) // 11

	// 7. String Membership (Using strings.Contains)
	fmt.Println(strings.Contains(myStr, "H")) // true
	fmt.Println(strings.Contains(myStr, "z")) // false

	// 8. String Iteration
	for _, s := range myStr {
		fmt.Printf("%c ", s) // H e l l o   W o r l d
	}
	fmt.Println()

	// 9. String Comparison
	str3 := "World"
	fmt.Println(str1 == str2) // true
	fmt.Println(str1 == str3) // false

	// 10. String Formatting
	name := "Alice"
	age := 25
	fmt.Printf("Hello, my name is %s and I am %d years old.\n", name, age) // Hello, my name is Alice and I am 25 years old.
	
	// 11. String Formatting using fmt.Sprintf
	s := fmt.Sprintf("Hello, my name is %s and I am %d years old.", name, age)
	fmt.Println(s) // Hello, my name is Alice and I am 25 years old.

	// 12. String Formatting using fmt.Printf with f-string-like behavior (Go 1.13+)
	fmt.Printf("Hello, my name is %s and I am %d years old.\n", name, age) // Hello, my name is Alice and I am 25 years old.

	// 13. String Methods (Using strings package)
	myStrLower := "hello world"
	fmt.Println(strings.Title(myStrLower)) // Hello World
	fmt.Println(strings.ToUpper(myStrLower)) // HELLO WORLD
	fmt.Println(strings.ToLower(myStrLower)) // hello world
	fmt.Println(strings.Title(myStrLower)) // Hello World
	fmt.Println(strings.ToTitle(strings.ToLower(myStrLower))) // Hello World
	fmt.Println(strings.Count(myStrLower, "l")) // 3
	fmt.Println(strings.Index(myStrLower, "l")) // 2
	fmt.Println(strings.Index(myStrLower, "z")) // -1
	fmt.Println(strings.LastIndex(myStrLower, "l")) // 9
	// fmt.Println(strings.Index(myStrLower, "z")) // -1 (Would cause runtime error if used with Index)
	fmt.Println(strings.ReplaceAll(myStrLower, "world", "Alice")) // hello Alice
	fmt.Println(strings.HasPrefix(myStrLower, "hello")) // true
	fmt.Println(strings.HasSuffix(myStrLower, "world")) // true
	fmt.Println(strings.Split(myStrLower, " ")) // [hello world]
	fmt.Println(strings.Split(myStrLower, "l")) // [he "" o wor d]
	fmt.Println(strings.TrimSpace("   hello world   ")) // hello world
	fmt.Println(strings.TrimLeft("   hello world   ", " ")) // "hello world   "
	fmt.Println(strings.TrimRight("   hello world   ", " ")) // "   hello world"
	fmt.Println(unicode.IsLetter(rune(myStrLower[0]))) // true
	fmt.Println(unicode.IsDigit(rune(myStrLower[0]))) // false
	fmt.Println(unicode.IsLower(rune(myStrLower[0]))) // true
	fmt.Println(unicode.IsUpper(rune(myStrLower[0]))) // false
	fmt.Println(unicode.IsSpace(rune(' '))) // true

	// 14. String Join
	fmt.Println(strings.Join(strings.Split(myStr, ""), " ")) // H e l l o   W o r l d
	reversed := func(s string) string {
		runes := []rune(s)
		for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
			runes[i], runes[j] = runes[j], runes[i]
		}
		return string(runes)
	}
	fmt.Println(reversed(myStr)) // dlroW olleH

	// 15. String Reverse
	fmt.Println(reverseString(myStr)) // dlroW olleH

	// 16. String Palindrome
	str1Palindrome := "madam"
	fmt.Println(str1Palindrome == reverseString(str1Palindrome)) // true

	// 17. String to Integer
	numStr := "123"
	num, err := strconv.Atoi(numStr)
	if err != nil {
		fmt.Println("Error converting string to int:", err)
	} else {
		fmt.Println(num) // 123
		fmt.Printf("%T\n", num) // int
	}

	// 18. Integer to String
	num = 123
	numStr = strconv.Itoa(num)
	fmt.Println(numStr) // 123
	fmt.Printf("%T\n", numStr) // string

	// 19. String to List (Slice of runes)
	myStrList := []rune(myStr)
	fmt.Println(myStrList) // [72 101 108 108 111 32 87 111 114 108 100]

	// 20. List to String
	l := []rune{'h', 'e', 'l', 'l', 'o'}
	fmt.Println(string(l)) // hello

	// 21. String to Set (Using map for set-like behavior)
	myStrSet := make(map[rune]bool)
	for _, char := range myStr {
		myStrSet[char] = true
	}
	fmt.Println(myStrSet) // map[32:true 68:true 72:true 87:true 101:true 108:true 111:true 114:true 100:true]

	// 22. Set to String
	runes := []rune{'o', 'e', 'h', 'l'}
	fmt.Println(string(runes)) // oehl

	// 23. String to Dictionary (Using map)
	myStrDict := make(map[int]rune)
	for i, char := range myStr {
		myStrDict[i] = char
	}
	fmt.Println(myStrDict) // map[0:72 1:101 2:108 3:108 4:111 5:32 6:87 7:111 8:114 9:108 10:100]

	// 24. Dictionary to String
	d := map[int]string{
		0:  "h",
		1:  "e",
		2:  "l",
		3:  "l",
		4:  "o",
	}
	var dictStr []string
	for i := 0; i < len(d); i++ {
		dictStr = append(dictStr, d[i])
	}
	fmt.Println(strings.Join(dictStr, "")) // hello

	// 25. String to Tuple (Using slice of runes)
	myStrTuple := []rune(myStr)
	fmt.Println(myStrTuple) // [72 101 108 108 111 32 87 111 114 108 100]

	// 26. Tuple to String
	t := []rune{'h', 'e', 'l', 'l', 'o'}
	fmt.Println(string(t)) // hello
}

// Helper function to reverse a string
func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}