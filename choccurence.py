string=input("please enter wordd")
char=input("please enter your ch")
i=0
digits=0
while(i<len(string)):
    if(string[i]==char):
        digits=digits+1
        i=i+1
print("total num of times",char,"occurred",digits)      