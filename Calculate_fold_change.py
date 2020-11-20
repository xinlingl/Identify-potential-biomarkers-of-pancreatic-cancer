import math
def FoldChange(data1,data2):
    for index in range(0,len(data1)):
        subset1=data1[index]
        subset2=data2[index]
        if float(subset2)==0:
            print("N/A")
        else:
            ratio=float(subset1)/float(subset2)
            if ratio>0:
                foldchange=math.log(ratio,2)
                print(foldchange)
            else:
                print("N/A")
