print("\tSolving a Quadratic Equation")
a = float(input("Enter the value of A: "))
b = float(input("Enter the value of B: "))
c = float(input("Enter the value of C: "))

d = ((b ** 2) - (4 * a * c)) * 0.5

print("X = ", (-1 *b + d)/(2*a))
print("Y = ", (-1 *b - d)/(2*a))