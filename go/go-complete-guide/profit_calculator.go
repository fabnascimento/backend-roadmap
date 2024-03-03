package main

import "fmt"

func getUserInput(prompt string) float64 {
  value float64
  fmt.Print(prompt)
  fmt.Scan(&value)

  return value
}

func main() {
  revenue := getUserInput("Revenue: ")
  expenses := getUserInput("Expenses: ")
  taxRate := getUserInput("Tax rate: ")
}
