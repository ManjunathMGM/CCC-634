t1 = float(input("Enter the percentage for Teacher 1: "))
t2 = float(input("Enter the percentage for Teacher 2: "))
t3 = float(input("Enter the percentage for Teacher 3: "))
t4 = float(input("Enter the percentage for Teacher 4: "))
t5 = float(input("Enter the percentage for Teacher 5: "))
t6 = float(input("Enter the percentage for Teacher 6: "))
t7 = float(input("Enter the percentage for Teacher 7: "))

average = (t1 + t2 + t3 + t4 + t5 + t6 + t7) / 7

invitation = bool(input("Letter of Invitation? (true/false): "))
hod = bool(input("Permission from HOD? (true/false): "))

eligible = average > 80 and (invitation or hod)

print(f"\nAverage Percentage: {average}%")
print("Eligibility for Special Python Training Session - ", eligible)
