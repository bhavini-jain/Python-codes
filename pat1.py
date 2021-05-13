# printing a pattern
row = int(input("enter no of rows:"))
for r in range(1, row+1):
    for sp in range(1,row+1-r):
        print(" ",end="")
# loop for printing
    c = 1
    while c <= r:
        print(c, end="")
        c += 1
    else:
        print()        