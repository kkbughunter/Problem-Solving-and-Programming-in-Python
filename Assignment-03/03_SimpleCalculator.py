print("""
---- Simple Calculator ----
      1. Addition
      2. Subraction
      3. Multiplaction
      4. Division
      5. Exit
""")

opt = int(input("Enter your Option: "))
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if(opt == 1):
    print(f"Result: {a} + {b} = {a + b}")
elif(opt == 2):
    print(f"Result: {a} + {b} = {a - b}")
elif(opt == 3):
    print(f"Result: {a} + {b} = {a * b}")
elif(opt == 4):
    if(b == 0):
        print("0 Division Error...")
    print(f"Result: {a} + {b} = {a / b}")
else:
    print("Thank you")