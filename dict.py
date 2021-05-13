# creating a dict to store emp detail
empinfo = {12001:'ganesh', 12003 :' pragya', 12002 :'bhavini'}
print(empinfo) 
#iterating a dict
for item in empinfo:
    print( item, " : " , empinfo[item])
# adding new item
empinfo[12004] = 'sagar'
print(empinfo)
#update an item
empinfo[12003] = " pritam"
print(empinfo)
#deleting an item
del empinfo[12002]
# fuctions
print(len(empinfo))
print(str(empinfo))