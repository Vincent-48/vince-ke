n=7
for i in range(n,-n-1, -1):
    for _ in range(abs(i)):
        print(" ",end="")
    for _ in range(n, abs(i)-1,-1):
        print("$ ",end="")
    print()