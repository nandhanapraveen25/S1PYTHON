def pyramid(n):
    for i in range(1,n + 1):
        for j in range(1, i + 1):
            print(i * j, end=" ")
        print()
N=int(input("enter the number of steps: "))
pyramid(N)
