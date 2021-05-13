
books=[]
for items in range(5):
   title = input("enter book titels")
   books.append(title)
else:
    print(books)   
   
#searching
name = input("enter book title to search")

for item in books:
    if name in item:
        print( item )
