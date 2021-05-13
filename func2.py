def getbill(units):
    if units>=500:
        rate=7.5
    else:
        rate=5.0
    bill = units*rate
    return bill
    #print(" your bill is: %0.2f Rs" %bill)     

un = int(input("enter your units:")  )
getbill(un)
print(getbill(un))