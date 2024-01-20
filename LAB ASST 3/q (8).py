number = int((input("Enter a 5 digit even number: ")))
digits = (number // 10000) % 10 + (number // 1000) % 10 + (number // 100) % 10 + (number // 10) % 10 + (number % 10)
print("Sum of digits:", digits)
