number = int((input("Enter a 5 digit even number: ")))
if len(str(number)) != 5:
    print("not a 5 digit number")
else:
    digits = (number // 10000) % 10 + (number // 1000) % 10 + (number // 100) % 10 + (number // 10) % 10 + (number % 10)
    print("Sum of digits:", digits)
