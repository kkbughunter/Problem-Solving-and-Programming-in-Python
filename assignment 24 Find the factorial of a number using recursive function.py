# 24 Find the factorial of a number using recursive function
def rec(n):
    if n == 1:
        return n
    else:
        return n*rec(n-1)

n = int(input("Enter a number: (please enter above 0 )"))
print("The factorial of",n, "is", rec (n))