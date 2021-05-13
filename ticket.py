# calc ticket pric eof passenger
TD = int(input(" enter travelling distance:"))

if TD >=1000:
   rate = 0.75
   water = 75
   print(" please keep water of 5 liters")
elif TD >=700:
   rate = 0.85
   water = 64
   print(" please keep water of 4 liters")
elif TD >=400:
   rate = 0.95
   water = 54 
   print(" please keep water of 3 liters")
else:
   rate = 1.1
   water = 40
   print(" please keep water of 2 liters") 
ticket = TD*rate*1.1+water
print(" Ticket is : %0.2f Rs to travel %d kms" %( ticket, TD))  