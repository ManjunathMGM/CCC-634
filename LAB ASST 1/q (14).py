radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

surface_area = round((3.14 * radius * ((radius ** 2 + height ** 2) ** 0.5)), 2)

print(f"The surface area of the inscribed cone is: {surface_area}")
