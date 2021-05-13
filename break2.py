#using break
import random
str = "be  happy@always"
for ch in str:
    if ch is '@':
        break
    print(ch,end ="")    
else:
    print(" yes ,i knw without break")     



while True:
    no = int(random.random()*100)
    print(no)
    if no > 30:
        print("bye bye")
        break
else:
    print("done")        