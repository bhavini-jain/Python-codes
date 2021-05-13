college = "Tech@20"
print(college)
# iterating string
for ch in college:
    print(ch,end="")

#indexing
print()
print(college[3])
print(college[-5])

#ranging
print(college[2:5])
print(college[-5:1])
print(college[-2:7])
print(college[2:2])
 
 #slicing
print(college[2:]) #2 to end
print(college[ :11]) #0 to end
print(college[-5:]) 
print(college[ :-3])

#opertora
str = college+"UDR"
print(str)
#repetion
print(college*3)
#membership
if "smart" in " udaipur smart city":
    print("yes")
else:
    print("no")

 #raw string
name = "shruti"
balance = 3546.4
year = 2019 
str = r"hello %s\nyour balance is: \t%0.2f\tRs\n in the year od %d"%(name, balance,year)
print(str) 
txt = "hello {}, your balance is{} in{}".format(name,balance,year) 
print(txt)    

