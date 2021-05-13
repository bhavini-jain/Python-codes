# to clac gross salary
basic = int (input(" enter basic salary"))

if basic>=15000:
   ta = basic*0.1
   da = basic*0.15 
   hra= basic*0.2
else :

   ta = basic*0.15
   da = basic*0.2
   hra = basic*0.3
gross = basic+ta+da+hra
print(" enjoy, Gross Salary is : %0.2f Rs" %gross)
