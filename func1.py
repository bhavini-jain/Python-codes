#function def
def getgross(basic):
    'to calc gross salary'
    if basic>=15000:
        ta = basic*0.1
        da = basic*0.15
        hra = basic*0.2
    else:
        ta = basic*0.15    
        da = basic*0.2
        hra = basic*0.3
    gross = basic+da+ta+hra
    print(" enjoy,gross salary is: %0.2f rs" %gross)

#func calling
getgross(12000)
bs = int(input(" enter Basic Salary" ) )    
getgross(bs)
