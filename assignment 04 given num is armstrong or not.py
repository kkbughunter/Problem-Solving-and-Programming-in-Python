# find the given number is armstrong number or not armstrong.
# Definion 
# number of N digits which are equal to sum of Nth power of its digits

# Eg : input=153  total digits is 3 
# =>  = 1^3 + 5^3 + 3^3 
# =>  = 1 + 125 + 27 
# =>  ans = 153
# =>  if ans is  = to the given number means 
# (or) 3701 = 3*3*3*3 + 7*7*7*7 + 0*0*0*0 + 1*1*1*1
# =>  the given number is armstrong number


arm = int(input("Enter a number: "))
num=len(str(arm))
sum = 0
temp = arm
while temp > 0:
   digit = temp % 10
   sum =sum + digit ** num
   temp //= 10
if arm == sum:
   print(arm,"is an ARMSTRONG NUMBER")
else:
   print(arm,"is not an ARMSTRONG NUMBER")
