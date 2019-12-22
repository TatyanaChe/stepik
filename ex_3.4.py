import os
pathhome="/home/tanya/python/"
pathfile=os.path.join(pathhome,'inp.txt')
# print(pathfile)
pathfile1=os.path.join(pathhome,'out.txt')
# print(pathfile1)
# read
inp=open(pathfile,'r')
s=inp.readline()
# print(s)
inp.close()
# print("s[-2]",s[-2])
#
out = open(pathfile1, 'a')
for i in range(len(s)-1):
#     print("i= ", i)
    if s[i].isalpha():
        if ((s[i+1]).isdigit()):
            num = s[i + 1]
            if i<len(s)-2:
                if (s[i+2]).isdigit():
                    num = s[i+1] + s[i+2]
#             print("num=", num)
            out = open(pathfile1, 'a')
            out.write(str(s[i]) * (int(num)))
            out.close()
            # check
#             out = open(pathfile1, 'r')
#             print(out.read())
#             out.close()
        i+= 1
    else:
        i+=1
# check
out = open(pathfile1, 'r')
print(out.read())
out.close()