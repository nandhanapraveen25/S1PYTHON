a=input("enter a string:")
first=a[0]
c=a[-1]
result=c
for i in a[1:-1]:
        result+=i
result+=first
print(result)
