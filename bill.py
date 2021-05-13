# a program to calc bill of fruits
quant = input("enter fruits quantity:")
quant = int(quant)
rate = float(input("enter rate per kg"))
bill = quant*rate
print("please pay bill is : %0.2f Rs" %bill)