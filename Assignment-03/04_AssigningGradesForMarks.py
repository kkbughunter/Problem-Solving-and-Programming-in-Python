print("Assigning Grades for Marks")
mark = int(input("Enter your Mark: "))

if(mark > 100):
    print("Enter the correct mark...")
elif(mark <50):
    print("Your Grade is F")
elif(mark <= 60 and mark >= 50):
    print("Your Grade is E")
elif(mark <= 70):
    print("Your Grade is D")
elif(mark <= 80):
    print("Your Grade is C")
elif(mark <= 90):
    print("Your Grade is B")
elif(mark > 90):
    print("Your Grade is A")

