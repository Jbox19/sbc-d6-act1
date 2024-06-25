#problem 2
 
row = int(input("Row: "))
col = int(input("Col: "))
i = 0
while (i < col):
    j = 0
    while (j < row):
        if (i == 0 or i == col-1 or j == 0 or j == row-1):
            print("*",end="")
        else:
            print(" ",end="")
        j = j + 1 
    i = i + 1
    print()
