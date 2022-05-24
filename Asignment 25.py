#Q.no:25)Print the Fibonacci series using recursive function.
print("Q.no:25)Print the Fibonacci series using recursive function.")
print("answer:-")

def fib(x):
    if(x <= 1):
        return x
    else:
        return(fib(x-1) + fib(x-2))
a = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(0,a,1):
    fibonacci=fib(i)
    print(fibonacci)
print("The fibanacci series has been printed using recursive function")
