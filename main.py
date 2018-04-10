num = input("Enter the depth of traingle")

lis = [0,1,0]
def lis_summer(lis):
    retLis = [0]
    sum=0
    for i in range(len(lis)-1):
        sum = lis[i]+lis[i+1]
        retLis.append(sum)
    
    retLis.append(0)
    #print retLis
    return retLis
        
for i in range(1,num):
    print lis
    lis=lis_summer(lis)[:]
