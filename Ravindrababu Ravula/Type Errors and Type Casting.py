# Type Errors and Type Casting 00:01

# print(len(1234))   # TypeError: len() takes exactly one argument (0 given)

# num_char = len(input("Enter your name: "))
# print("Your name has " + num_char + " character")  # TypeError: can only concatenate str (not "int") to str

# Type casting 03:12
num_char = len(input("Enter your name: "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " character") 

# Typeof method 04:18
a = 10
print(type(a))
a = float(10)
print(type(a))
a = str(10)
print(type(a))

print(str(100) + str(200))
