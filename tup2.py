# tuple storing mix values
mix = ( 1230, 560.99, 5j+4, "IN@20", input("enter college name:"), 770,("in","DL" ,"RS"), 1250.76)
for item in mix:
    if type(item)==int or type(item)==float or type(item)==complex:
        print(item)


books = 'python', "java", '''android''',"cloud"
print(books)
balance = (1223000)
print(balance)
tup = ()
print(tup)
del books
print(books)