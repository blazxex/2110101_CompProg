def checkPass(com,cal1,cal2):
    if com=='A' and cal1<='C' and cal2<='C':
        return True
    else:
        return False

def checkMaxNum(a,b):
    if a>b:
        return True
    elif a<b:
        return False
    else:
        return 404
    
def checkMax(a,b):
    if a<b:
        return True
    elif a>b:
        return False
    else:
        return 404

def choose(stu1,stu2):
    pas=[]
    gpa_1,com_1,cal1_1,cal2_1 = stu1[1],stu1[2],stu1[3],stu1[4]
    gpa_2,com_2,cal1_2,cal2_2 = stu2[1],stu2[2],stu2[3],stu2[4]
    passOne = checkPass(com_1,cal1_1,cal2_1)
    passTure = checkPass(com_2,cal1_2,cal2_2)
    if passOne != passTure:
        if passOne == True:
            pas.append(stu1[0])
        else:pas.append(stu2[0])
    elif passOne==passTure:
        if passOne == False:
            pass
        else:
            if checkMaxNum(gpa_1,gpa_2) == True:
                pas.append(stu1[0])
            elif checkMaxNum(gpa_1,gpa_2) == False:
                pas.append(stu2[0])
            else:
                if checkMax(com_1,com_2) == True:
                    pas.append(stu1[0])
                elif checkMax(com_1,com_2) == False:
                    pas.append(stu2[0])
                else:
                    if checkMax(cal1_1,cal1_2) == True:
                        pas.append(stu1[0])
                    elif checkMax(cal1_1,cal1_2) == False:
                        pas.append(stu2[0])
                    else:
                        if checkMax(cal2_1,cal2_2) == True:
                            pas.append(stu1[0])
                        elif checkMax(cal2_1,cal2_2) == False:
                            pas.append(stu2[0])
                        else:
                            pas.append(stu1[0])
                            pas.append(stu2[0])
                            
    return pas
    
    
    
    
    


             
        
exec(input())