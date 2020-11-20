from operator import itemgetter
def getKey(item):
 return abs(float(item[4]))

def getanoKey(anoitem):
 return float(anoitem[5])

def main(f1,f2):
    count=0
    result=[]
    newl=[]
    finalresult=[]
    dictionary={}
    reference={}
    for line in f1:
        count=count+1
        listofitem=line.split()
        zscore=listofitem[2]
        for index in range(0,len(listofitem)):
            item=listofitem[index]
            if item[0:2]=="uc" and zscore!='N/A' and item not in dictionary:
                dictionary[item]=float(zscore)
                reference[item]=listofitem[0]
                result.append(item)
            elif item[0:2]=="uc" and zscore!='N/A' and item in dictionary:
                total=dictionary[item]+float(zscore)
                dictionary[item]=total/2

    for line in f2:
        line=line.split()
        if line[0] in dictionary and line[3]!='N/A':
            anostring=(reference[line[0]],line[0],line[1],line[2],line[3],dictionary[line[0]])
            finalresult.append(anostring)
    l=sorted(finalresult, key=getKey)
    anol=sorted(finalresult, key=getanoKey)

    index=len(l)-1
    while index>0:
        newl.append(l[index])
        index=index-1

    f=open("C:/Python34/output_file(2).txt",'w')
    string="name_of_gene"+'   '+"isoform_id"+'   '+"z-score_of_RNA_samples"+'   '+"z-score_of_RNA_controls"+'   '+"fold_change"+'   '+"z-score_of_protein_samples"+'\n'
    f.write(string)
    
    for i in range(0,len(newl)):
        anostring=str(newl[i][0])+'   '+str(newl[i][1])+'   '+str(newl[i][2])+'   '+str(newl[i][3])+'   '+str(newl[i][4])+'   '+str(newl[i][5])+'\n'
        if float(newl[i][4])>5 and float(newl[i][2])>0 and float(newl[i][5])>0:
            f.write(anostring)
        elif float(newl[i][4])<-5 and float(newl[i][2])<0 and float(newl[i][5])<0:
            f.write(anostring)

                                                        
