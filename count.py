text=input("enter the text:")
word=text.split()
t={}
for i in word:
    if i in t:
        t[i]+=1
    else:
        t[i] = 1
print(t)