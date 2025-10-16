a=input("enter the first list:")
b=input("enter the second list:")
x=len(a)
y=len(b)
if x==y:
    print("both length are same ")
else:
    print("not same length")

s1=0
s2=0
for i in a:
    i=int(i)
    s1+=i
for j in b:
    j=int(j)
    s2+=j
if s1==s2:
    print("the sum of both list are same")
else:
    print("the sum of both list are different")


for i in a:
    for j in b:
        if i==j:
            print(f"the value {i} occur in both")
        else:
            print(f"values {i} does not occur in both")
