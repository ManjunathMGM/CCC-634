print("1st Ques")

data1 = 15
data2 = "DATA"
print(type(data1), type(data2))

print("----------------------------------")

print("2nd Ques")

num = float(input("Enter your Number: "))
num_op = format(num, ".2f")
print(f"Output = {num_op}")

print("----------------------------------")

print("3rd Ques")

str1 = input("Enter String 1")
str2 = input("Enter String 2")
str3 = input("Enter String 3")

print(str1 + str2 + str3)

print("----------------------------------")

print("4th Ques")

cp1 = complex(input("Enter a Complex Number 1"))
cp2 = complex(input("Enter a Complex Number 2"))
plus = cp1 + cp2
subt = cp1 - cp2

print("Addition:", plus, "Subtraction:", subt)

print("------------------------------------------------")

print("5th Ques")

i_ishan = int(input("Enter Ishan's Income"))
i_hari = int(input("Enter Hari's Income"))
i_charu = int(input("Enter Charu's Income"))
i_william = int(input("Enter William's Income"))

com1 = i_ishan + i_hari < i_charu + i_william
com2 = i_ishan + i_hari == i_charu + i_william
com3 = i_ishan + i_hari > i_charu + i_william

print(f"1. {com1} \n2. {com2} \n3. {com3}")

print("------------------------------------------------------------")

print("6th Ques")

poem = "There once was a fly on the wall,\nI wonder, why didn’t it fall?\nBecause its feet stuck? Or was it just luck?\nOr does gravity miss things so small?"
print(poem)

print("------------------------------------------------------------------")

print("7th Ques")

jump = 13.5
distance = float(input("Enter the Distance: "))
steps = distance // 13.5 + 1
print(f"Steps required for the Grey Kangaroo to travel {distance} meters is {steps}")

print("------------------------------------------------------")

print("8th Ques")

number = int((input("Enter a 5 digit even number: ")))
if len(str(number)) != 5:
    print("not a 5 digit number")
else:
    digits = (number // 10000) % 10 + (number // 1000) % 10 + (number // 100) % 10 + (number // 10) % 10 + (number % 10)
    print("Sum of digits:", digits)

print("--------------------------------------------------------------------------")

print("9th Ques")

l = float(input("Enter the length of a wire: "))
n = int(input("Enter the number of sides of a polygon: "))
len_side = round((l / n), 2)
print(f"Length of each side is {len_side}")

print("---------------------------------------------------------------------------")

print("10th Ques")

sec = int(input("Enter the amount of seconds: "))
hours = sec // 3600
r_seconds = sec % 3600
min = r_seconds // 60
seconds = r_seconds % 60

print(f"{sec} seconds = {hours} hours, {min} minutes, and {seconds} seconds.")

print("-------------------------------------------------------------------------------")

print("11th Ques")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Bitwise AND:", num1 & num2)

print("Bitwise OR:", num1 | num2)

print("Bitwise NOT (num1):", ~num1)
print("Bitwise NOT (num2):", ~num2)

print("Bitwise XOR:", num1 ^ num2)

print("Bitwise right shift (num1):", num1 >> 1)
print("Bitwise right shift (num2):", num2 >> 1)

print("Bitwise left shift (num1):", num1 << 1)
print("Bitwise left shift (num2):", num2 << 1)

print("--------------------------------------------------------------")

print("12th Ques")
ip1 = input("Enter the 1st boolean value (True/False): ").lower()
ip2 = input("Enter the 2nd boolean value (True/False): ").lower()

v1 = ip1 == "true"
v2 = ip2 == "true"

print(v1, v2)

result_and = v1 and v2
result_or = v1 or v2
result_not1 = not v1
result_not2 = not v2

print("Results:")
print(f"AND - {result_and}")
print(f"OR - {result_or}")
print(f"NOT for the first value - {result_not1}")
print(f"NOT for the second value - {result_not2}")

print("-----------------------------------------------------")

print("13th Ques")

t1 = float(input("Enter the percentage for Teacher 1: "))
t2 = float(input("Enter the percentage for Teacher 2: "))
t3 = float(input("Enter the percentage for Teacher 3: "))
t4 = float(input("Enter the percentage for Teacher 4: "))
t5 = float(input("Enter the percentage for Teacher 5: "))
t6 = float(input("Enter the percentage for Teacher 6: "))
t7 = float(input("Enter the percentage for Teacher 7: "))

average = (t1 + t2 + t3 + t4 + t5 + t6 + t7) / 7

invitation = (input("Letter of Invitation? (yes/no): ")).lower()
hod = (input("Permission from HOD? (yes/no): "))

eligible = average > 80 and (invitation == "yes" or hod == "yes")

print(f"\nAverage Percentage: {average}%")
print("Eligibility for Special Python Training Session - ", eligible)

print("------------------------------------------------------------------------")

print("14th Ques")

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

surface_area = round((3.14 * radius * ((radius ** 2 + height ** 2) ** 0.5)), 2)

print(f"The surface area of the inscribed cone is: {surface_area}")

print("---------------------------------------------------------------------------")

print("15th Ques")

drop_per_sec = 1
seconds_in_day = 24 * 60 * 60  # 86400
days = int(input("Enter the no. of days: "))

total_drops = drop_per_sec * seconds_in_day * days
waste = total_drops / 8000  # 800 drops = 100ml

print(f"The liter count of water wasted in {days} days is: {waste:} liters")

print("-------------------------------------------------------------------------------")

print("16th Ques")

n = int(input("Enter the number of balls: "))
m = int(input("Enter the max no. of balls per box: "))
min_boxes = (n + m - 1) // m

print(f"The min no. of boxes required is: {min_boxes}")

print("------------------------------------------------------------------------------------")

print("17th Ques")

real1 = float(input("Real part of the 1st no. "))
imag1 = float(input("Imaginary part of the 1st no. "))

real2 = float(input("Real part of the 2nd no. "))
imag2 = float(input("Imaginary part of the 2nd no. "))

complex1 = complex(real1, imag1)
complex2 = complex(real2, imag2)
product = complex1 * complex2

print(product)
print(type(product))

print("-------------------------------------------------------------------------")

print("18th Ques")

basic = float(input("Enter Ayush basic salary: "))
hra = basic * 0.12
da = basic * 0.4
pf = (basic + da) * 0.1
net_salary = basic + hra + da - pf
total_pf = basic * 12

print("Net Salary: ", net_salary)
print("Total PF contribution: ", total_pf)

print("-------------------------------------------------------------------------")
