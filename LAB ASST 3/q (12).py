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
