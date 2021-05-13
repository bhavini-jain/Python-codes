# to calc a bill of electricity
units =int( input( " enter no of units"))


if units>=500:
  rate =7.5
  print(" rate per unit is : %0.2f Rs" %rate ) 
else:
  rate =5.0
  print(" rate per unit is : %0.2f Rs" %rate)
bill = units*rate*1.10
print(" please pay bill is : %0.2f Rs" %bill) 