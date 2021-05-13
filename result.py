# to print result 
eng = int(input("enter english marks:"))
math = int( input("enter maths marks"))
science =int( input("enter sci marks"))
average = eng+math+science
if eng>100 or math>100 or science>100 or eng<0 or sci<0 or math<0:
    print(" invalid marks")
else:    
    per = average/3

    if per>=80:
       print("honours with %0.2f marks" %per)
    elif per>=60:
       print(" 1st division with %0.2f marks  "%per )
    elif per>=50:
       print(" 2nd division with %0.2f marks" %per)
    elif per>=40:
       print(" 3rd division with %0.2f marks"%per)
    else:
       print("fail")     

