def loanel(basic,bonus,fd):
    'to calc loan elligiblity'
    if basic>=20000:
        loan = basic*5
    else:
        loan = basic*4
    if bonus>=10000:
        loan +=bonus*3
    else:
        loan += bonus*2
    loan +=fd*0.5
    return loan

#req aegu(positional order)
amt = loanel(22000,12000,60000)
print("u can get loan upto : %0.2f Rs" %amt)
#keyword argu
print( loanel(fd=40000,basic=14000,bonus=7000))   
#default argu
#amt = loanel(16000,6000)                 
print("u can get loan upto: %0.2f rs "%amt)