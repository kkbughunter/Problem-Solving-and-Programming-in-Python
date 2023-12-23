# To  write  a  Python  program  to  calculate  the  area  of  different 
# common two-dimensional shapes, i.e. that of a square, 
# rectangle, triangle or circle, based on the user’s input. 
PI = 3.14

print("""
Area of Shapes:
    1. Square
    2. Rectangle
    3. Triangle
    4. Circle 
""")

print("\t1. Square")
side = float(input("Enter the side: "))
print("Area of an Square: ", side * side)

print("\t2. Rectangle")
length = float(input("Enter the length: "))
breadth = float(input("Enter the Breadth: "))
print("Area of an Rectangle: ", length * breadth)

print("\t3. Triangle")
base = float(input("Enter the Base: "))
height =  float(input("Enter the value of height: "))
print("Area of Triangle: ", 0.5 * base * height)

print("\t4. Area of Circle")
radius = float(input("Enter the Raduis: "))
print("Area of an Circle: ", PI * radius * radius)

print("\n\t\tThank you...")