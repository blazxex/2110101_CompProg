# import urllib.request

# def find(s, start, c):
#     for i in range(start, len(s)):
#         if s[i] == c: return i
#     return -1

# url = "http://air4thai.pcd.go.th/services/getNewAQI_XML.php?stationID=52t"
# web = urllib.request.urlopen(url)
# for line in web:
#     line = line.decode()
#     if "<PM25 value=" in line:
#         i = find(line, 0, '"')
#         j = find(line, i+1, '"')
#         print("PM 2.5 =", line[i:j])
#         break

# s = '1235rewfadsf'
# # print(s[::-1])
# def thousands_separator(n):
#     x = str(n)
#     num = len(x)
#     mo = (num%3)
#     y=''
#     if mo!= 0:
#         y=x[:mo]+','
#     for i in range(mo,len(x)-2,3):
#         y += x[i:i+3]+','
#     return y[:len(y)-1]
# print(thousands_separator(101))

# fin = open('data.txt','r')
# lin = fin.readline()
# print(lin[:-1])
# for lin in fin:
#     print(lin[:-1])
# fin.close()

# a='sdad'
# print(a[0:0])
# print(ord('s'),ord('B'))
# print((2<2))
print(4**5//2)