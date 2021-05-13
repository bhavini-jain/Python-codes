msg = input("enter text:")
alpha,digit,space,symbol = 0,0,0,0

for ch in msg:
    if ch.isalpha():
        alpha+=1
    elif ch.isdigit():
        digit+=1
    elif ch.isspace():
        space+=1
    else:
        symbol+=1
else:
    print("digits : %d\nalphabets :%d\nspaces %d\nsymbols %d:"\
    %(digit,alpha,space,symbol)    )
    size = len(msg)
    print("size: %d" %size)
    if symbol>=size*0.2:
        print("meaningfuless")
    else:
        print("meaningful")    