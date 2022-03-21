# Define a function that can accept two strings as input and
#  print the string with maximum length in consol

def leng(y):
     return max(y,key=len)
x=input("Enter two string : ")
print(leng(x.split()))

