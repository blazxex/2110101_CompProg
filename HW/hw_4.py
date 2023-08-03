scan_data = "-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,-,+,-,-,-,-,-,-,-,-"
scan_data_2 = "+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-,+,-"
data_list = scan_data_2.split(',')
print(len(data_list))
size = -1
i = 1
while size**3< len(data_list): 
    size = i
    i+=1

data_matrix = []
i=0
for j in range(size,size**3+1,size):
    data_matrix.append([''.join((data_list[i:j]))])
    i = j
print((data_matrix))



def max_height(data_matrix):
    defect_index = []
    for  i,x in enumerate(data_matrix): 
        for j,y in enumerate(x):
            if y == '+':
                defect_index.append([(i//size)+1,j])    
    print(defect_index)    

max_height(data_matrix)
        
    
