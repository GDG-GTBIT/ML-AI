#star pattern 
n = int(input("enter number: "))
print(n)
i = 1
j = 0
while(i<=n):
    while(j<=i-1):
        print("* ",end="") 
        j += 1
    print("\r") 
    i += 1
