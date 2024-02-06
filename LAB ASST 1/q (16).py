
n = int(input("Enter the number of balls: "))
m = int(input("Enter the max no. of balls per box: "))
min_boxes = (n + m - 1) // m

print(f"The min no. of boxes required is: {min_boxes}")
