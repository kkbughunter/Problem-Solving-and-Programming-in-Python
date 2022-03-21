# print the N fibonaccio serise 

print("Find the Fibonacci serise")
fi=int(input("Enter your number :"))
a=0
b=1
print("The Fibonacci serise is",a)
print("The Fibonacci serise is",b)
for i in range(2,fi):
    ans=a+b
    a=b
    b=ans
    print("The Fibonacci series is",ans)
