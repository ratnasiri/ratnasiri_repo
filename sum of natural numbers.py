num=int(input("enter a num"))
if num < 0:
    print ("enter a positive num")
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
    print("the sum is",sum)
        
