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
    

stid_1,gpa_1,com_1,cal1_1,cal2_1 = input().split()
stid_2,gpa_2,com_2,cal1_2,cal2_2 = input().split()


passOne = checkPass(com_1,cal1_1,cal2_1)
passTure = checkPass(com_2,cal1_2,cal2_2)

if passOne != passTure:
    if passOne == True:
        print(stid_1)
    else:print(stid_2)
elif passOne==passTure:
    if passOne == False:
       
        print('None')
    else:
        if checkMaxNum(gpa_1,gpa_2) == True:
            print(stid_1)
        elif checkMaxNum(gpa_1,gpa_2) == False:
            print(stid_2)
        else:
            if checkMax(com_1,com_2) == True:
                print(stid_1)
            elif checkMax(com_1,com_2) == False:
                print(stid_2)
            else:
                if checkMax(cal1_1,cal1_2) == True:
                    print(stid_1)
                elif checkMax(cal1_1,cal1_2) == False:
                    print(stid_2)
                else:
                    if checkMax(cal2_1,cal2_2) == True:
                        print(stid_1)
                    elif checkMax(cal2_1,cal2_2) == False:
                        print(stid_2)
                    else:
                        print('Both')
            
        
