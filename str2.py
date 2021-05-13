str =input("enter your string")
vowels = 0
spaces = 0
digits = 0
for ch in str:
  if ch in "aeiouAEOIU" :
     vowels+=1
     
  elif ch in " " :
     spaces+=1
     
 
  elif ch in "0123456789":
     digits+=1
else:
    print("digit: %d\nvowels: %d\nspaces: %d" %(digits,vowels,spaces))     
    