def FindAverageControls(f):
    i=0
    total=0
    temp=[]
    answer=[]
    finalanswer=[]
    for lines in f:
        if "V1" not in lines:
            for index in range(0,len(lines)):
                if lines[index]!=' ' and lines[index]!='\n':
                    temp.append(lines[index])
            while i<len(temp) and '\t' in temp:
                ind=temp.index('\t')
                item=lines[i:ind]
                answer.append(item)
                temp[ind]='none'
                i=ind+1
            i=0
            item=lines[ind+1:len(lines)-1]
            answer.append(item)
            j=len(answer)-3
            while j<len(answer):
                total=total+float(answer[j])
                j=j+1
            average=total/3
            total=0
            finalanswer.append(average)
            temp=[]
            answer=[]
            j=len(answer)-3
    f2=open("averageforcontrolsPCA.txt",'w')
    for index in range(0,len(finalanswer)):
        f2.write(str(finalanswer[index]))
        f2.write(' ')
