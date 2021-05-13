import math
def getbill(units,rate):
    'to calc bill'
    bill = units*rate
    return bill

bill = lambda units ,rate:print("bill is : %0.2f rs " %(units*rate))
cylinder = lambda radius,height:\
    print("area is: %0.2f"%(math.pi*radius*height))

bill(400,7.5)
cylinder(30,10)    