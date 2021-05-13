# to find largest of 3 no
x = float(input(" enter x:"))
y = float(input(" enter y:"))
z = float(input(" enter z:"))
if x>y:
   if x>z:
      print("x=%0.2f is greatest " %x)
   else:
      print("z=%0.2f is greatest "%z)
else:
   if y>z:
      print("y=%0.2f is greatest" %y)
   else:
      print("z=%0.2f is greatest" %z)
 