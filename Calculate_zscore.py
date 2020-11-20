import math
def FindZScore(data):
    k=0
    newdata=[]
    while k<len(data)-29:
        line=data[k:k+30]
        newdata.append(line)
        k=k+30
        
    answer=[[0 for j in range(0,len(newdata[0]))] for i in range(0,len(newdata))]
    total=0
    total2=0
    newtotal=0
    newtotal2=0
    sumofsquaredifference=0
    sumofsquaredifference2=0
    newind=0
    i=0
    i2=0
    count=0
    count2=0
    result=[]
    
    for index in range(0,len(newdata[0])-3):
        i=0
        while i<len(newdata):
            item=newdata[i][index]
            total=total+float(item)
            i=i+1
        average=total/len(newdata)
        total=0
        sumofsquaredifference=0
        for j in range(0,len(newdata)):
            newitem=newdata[j][index]
            difference=float(newitem)-average
            squaredifference=difference*difference
            sumofsquaredifference=sumofsquaredifference+squaredifference
        variance=sumofsquaredifference/len(newdata)
        standardeviation=math.sqrt(variance)
            

        for z in range(0,len(newdata)):
            newitem2=newdata[z][index]
            if standardeviation!=0:
                zscore=(float(newitem2)-average)/standardeviation
            else:
                zscore='N/A'
            answer[z][index]=zscore

    for ind in range(0,len(answer)):
        newind=0
        while newind<len(answer[0])-3:
            newitem2=answer[ind][newind]
            if newitem2!='N/A':
                newtotal=newtotal+newitem2
                count=count+1
            newind=newind+1
        newaverage=newtotal/count
        count=0
        newtotal=0


    for index2 in range(len(newdata[0])-3,len(newdata[0])):
        i2=0
        while i2<len(newdata):
            item2=newdata[i2][index2]
            total2=total2+float(item2)
            i2=i2+1
        average2=total2/len(newdata)
        total2=0
        sumofsquaredifference2=0
        for j in range(0,len(newdata)):
            newitem3=newdata[j][index]
            difference2=float(newitem3)-average2
            squaredifference2=difference2*difference2
            sumofsquaredifference2=sumofsquaredifference2+squaredifference2
        variance2=sumofsquaredifference2/len(newdata)
        standardeviation2=math.sqrt(variance2)
            

        for z2 in range(0,len(newdata)):
            newitem4=newdata[z2][index2]
            if standardeviation2!=0:
                zscore2=(float(newitem4)-average2)/standardeviation2
            else:
                zscore2='N/A'
            answer[z2][index2]=zscore2

    print("controls")     
    for ind2 in range(0,len(answer)):
        newind2=len(answer[0])-3
        while newind2<len(answer[0]):
            val=answer[ind2][newind2]
            if val!='N/A':
                newtotal2=newtotal2+val
                count2=count2+1
            newind2=newind2+1
        newaverage2=newtotal2/count2
        count2=0
        newtotal2=0
        print(newaverage2)
    
