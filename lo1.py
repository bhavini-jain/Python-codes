str = input("enter text")

vowel =0
for ch in str:
    if ch in "aeiouAEIOU":
        print(ch,end="")
        vowel+=1
else:
    print("\n%d vowels in : \n%s"%(vowel,str))        