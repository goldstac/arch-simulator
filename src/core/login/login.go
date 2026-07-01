package main

import "fmt"

func main() {
	var username string
	var passwd string
	fmt.Println("Welcome To Arch Linux")
	fmt.Println("Enter Username")
	fmt.Scan(&username)
	if username == "admin" {
		fmt.Println("Username Correct")
		fmt.Println("Enter Password")
		if passwd == "iusearchbtw" {
			fmt.Println("Password Succsesful")
			fmt.Println("Welcome", username)
		} else {
			fmt.Println("Password Incorrect")
		}
	} else {
		fmt.Println("Username Incorrect")
	}

}
