a=input("enter a string:")
first=a[0]
result=first
for i in a[1:]:
    if(i==first):
        i="$"
        result+=i
    else:
        result+=i
print(result)

