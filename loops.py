#Using for loop 
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")
    
#Using while loop
rows = int(input("Enter number of rows: "))
i = 0
while i < rows:
    j = 0
    while j <= i:
        print(j+1, end = " ")
        j=j+1
    i=i+1
    print("\n")
