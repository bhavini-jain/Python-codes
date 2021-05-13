def gamescore(team, *runs):
    'to find game score and centuries'
    sum = 0
    century = 0
    for item in runs:
        sum+=item
        if item>=100:
            century+=1
    else:
        print("score of %s is %d runs with %d centuries" %(team,sum,century))


#calling a fun
gamescore( "IND" , 55,120,52,75,23)
gamescore("PAK" , 7,4,12,1,5,85,12,6,0,3)          
gamescore("ENG",65,40)