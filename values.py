num=input("enter the list of integers:")
number=num.split()
list=[]
for i in number:
    i=int(i)
    if(i>100):
        list.append("over")
    else:
        list.append(i)
print(list)