# creating tupe to store marks
marks =( 92, 84, 72, 56,65,92)
print(marks)
# iterating marks
for item in marks:
    print(item)
 #indexing
print( marks[2] ) 
print( marks[-2] )
 #ranging
print(marks[2:5])
print(marks[5:-3])
print(marks[2: ])
print(marks[ :7])
print(marks[-2: ])
#functions
print( len(marks))
print( max(marks))
print( min(marks))
t = tuple("BHAVINI")
print(t)
#methods
print( marks.count(92))
print( marks.index(92))
