a=int(input("enter a first number: "))
b=int(input("enter a second number: "))
c=int(input("enter a third number: "))
if(a>b):
    if(a>c):
        print(f" biggest number is",a)
elif(a<c):
        print(f" biggest number is", c)
elif(b>a):
    if(b>c):
        print(f" biggest number is", b)
