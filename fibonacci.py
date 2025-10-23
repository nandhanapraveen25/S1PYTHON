def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a,end="")
        a,b=b,a+b
N=int(input("enter the number of terms:"))
print("fibnoacci series")
fibonacci(N)