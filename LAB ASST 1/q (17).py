real1 = float(input("Real part of the 1st no. "))
imag1 = float(input("Imaginary part of the 1st no. "))

real2 = float(input("Real part of the 2nd no. "))
imag2 = float(input("Imaginary part of the 2nd no. "))

complex1 = complex(real1, imag1)
complex2 = complex(real2, imag2)
product = complex1 * complex2

print(product)
print(type(product))
