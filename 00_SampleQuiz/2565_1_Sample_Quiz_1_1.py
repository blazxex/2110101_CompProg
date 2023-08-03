# num = [int(x) for x in input().split()]
# k = int(input())
# sum_list = sum(num)
# sum_same = 0 
# count=0
# for i in range(len(num)-1):
#     if num[i]==num[i+1]:
#         if count==0:
#             count+=2
#         else: count+=1
        
#     elif num[i]!=num[i+1]:
#         if count>=k:
#             sum_same+= num[i]*count
#             # print(num[i],count)
#             count = 0
# # print(sum_same)
# print(sum_list-sum_same)

# num = [int(x) for x in input().split()]
# k = int(input())
# sum_list = sum(num)
# sum_same = 0 
# count=1
# for i in range(len(num)-1):
#     if num[i]==num[i+1]:
#         count+=1
#     else:
#         if count>=k:
#             sum_same+= num[i]*count
#         count=1
#     if i == len(num)-2 and count>=k:
#         sum_same+= num[i]*count
#         break
# print(sum_list-sum_same)

# string_input = '112222341'

# # Create an empty list to hold the counts of each character
# char_counts = []

# # Loop over each character in the input string and update the count in the list
# for char in string_input:
#     found = False
#     for i in range(len(char_counts)):
#         if char_counts[i][0] == char:
#             char_counts[i][1] += 1
#             found = True
#             break
#     if not found:
#         char_counts.append([char, 1])

# # Print out the results in the specified format
# for char_count in char_counts:
#     print(char_count[0], char_count[1])
