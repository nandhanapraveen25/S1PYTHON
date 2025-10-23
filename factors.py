def factors(n):
    result=[]
    for i in range(1, n + 1):
        if n%i==0:
            result.append(i)
    return result
num=int(input("enter a number: "))
print("factors of",num,"are:",factors(num))