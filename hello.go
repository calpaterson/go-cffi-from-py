package main

import "C"
import "fmt"

//export Hello
func Hello(){
	fmt.Printf("Hello, World!\n")
}

func main() {}
