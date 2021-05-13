milks = [1.5,2.25,0.5,3.5,1.25,4.5]
print(milks)
sum = 0

for item in milks:
    print( item )
    sum+=item
else:
    bill = sum*40
    print(" bill is : %0.2f rs" %bill)

#indexing
print(milks[3]) 
print( milks[2:6]) 
print(milks[ :-2])
milks.append(5.5)
print(milks)
#update an item
milks[3] = 5.5
print( milks)
#del an item
del milks[2]
print(milks)
#functions
size = len( milks )
print(size)
print(max(milks))
print(min(milks))
t = list("techno@20")
print(t)