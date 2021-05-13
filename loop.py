range(5)       #0,1,2,3,4
range(3,7)     #3,4,5,6
range(4,13,3)  #4,7,10
range(40,9,-5) #40,35,30,25,20,15,10

for x in range(5):
    print("x =%d" %x)

print("--------")
for item in range(4,13,3):
    print("item :%d" %item)
else:
    print("yeah,done")

 str ="UDRINDIA@20"
 for ch in str:
    if ch in "AEIOU":
        print(ch, end="")    
