# creating a dict to store 
books ={ 1201: 'andoid',1202:"python", 1203:"java", 1204:"cloud"}
print(books)
# returns a copy of dict
dt = books.copy()
print( dt )
# returns a dict by iterating given seq
print( books.fromkeys("INDIA@20", 1000))
# returns a value of given key
print(books.keys() )
# returns a value of given values
print(books.values() )
# add new item if not exist
books.setdefault(1205, " web design")
print(books)
# updating 
books.update({ 1206: " googleweb", 1207:"maths"})
print(books)
# returns lists of tuple
print(books.items())

