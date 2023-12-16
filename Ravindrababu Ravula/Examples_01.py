# Examples 01
# EVEN or ODD 0:09 
number = int(input("Enter a numbaer: "))
if number % 2 == 0:
    print("This is a even number.")
else:
    print("This is a odd number.")


# Calculate BMI 1:59 
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your DMI is {bmi}, you are under weight.")
elif bmi < 25:
    print(f"Your DMI is {bmi}, you are Normal weight.")
elif bmi < 30:
    print(f"Your DMI is {bmi}, you are Overweight.")
elif bmi < 35:
    print(f"Your DMI is {bmi}, you are obese.")
else:
    print(f"Your DMI is {bmi}, you are clinically obese.")


# Leap year 5:12 
year = int(input("Which Year do you want to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leak Year")
        else:
            print("Not Leap year")
    else: 
        print("Leak Year")
else:
    print("Not Leak Year")


# Pizza order program 9:30
print("---Welcome to pizza Deliveries---")
size = input("What size pizza do you want: S ,M or L: ")
add_pepperoni = input("Do you want to pepperoni : Y or N : ")
extra_cheese = input("Do you want to extra cheese : Y or N : ")

bill = 0
if size == 'S':
    bill = 100
elif size == 'M':
    bill += 200
elif size == 'L': 
    bill += 300

if add_pepperoni == "Y":
    if size == 'S':
        bill += 20
    else: 
        bill += 30

if extra_cheese == "Y":
    bill += 10

print(f"Your final bill is {bill}")


