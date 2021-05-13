# creating a dict to store account detail
actinfo ={}

for i in range(4):
    # user input
    an = int(input("enter ac no:"))
    ahn = input("enter ac holder name")
    ab = float(input ("enter ac balance"))
    pin = int( input(" enter pin:"))
    # adding into dict
    actinfo[an]=[ahn,ab,pin]
else:
    print( actinfo)  
# searchin an account    
item = int(input( "enter your ac no"))      
if  item in actinfo:
    print( item,":" ,actinfo[item])        
else:
    print("invalid acoount") 

