import os
import operator
pathhome="/home/tanya/python/"
pathfile=os.path.join(pathhome,'dataset_3363_3.txt')
# read
inp=open(pathfile,'r')
s=inp.read().lower().split()
print(s)
inp.close()
#
sort=sorted(s)
print("sort ",sort)
dict={}
num=1
dist=[]
#distinct
for i in range(len(sort)-1):
    if sort[i] not in dist:
        dist.append(sort[i])
    else:
        i+=1
print("dist =",dist)
#count distinct
for i in range(len(dist)):
    num=sort.count(dist[i])
    if (num,dist[i]) in dict:
        i+=1
    else:    
        dict[dist[i]]=num
    i+=1
print("dict ",dict)
#
# stats = {'a':1000, 'b':3000, 'c': 100, 'd':3000}
# inverse = stats.
# print(max(stats.items(), key=operator.itemgetter(1))[0])
maximum=max(dict.items(), key=operator.itemgetter(1))[0]
print(maximum, dict.get((maximum),num))
# #tuple' object
# print(max(zip(stats.values(), stats.keys())))
# print(max(zip(dict.values(), dict.keys())))
# maximum=max(zip(stats.keys(),stats.values()))
# print("maximum", *maximum)
# maximum=max(zip(dict.values(),dict.keys()))
# inverse=maximum.reverse()
# print("inverse", *inverse)
# print("maximum", *maximum)
#
# inverse=dict.reverse()
# print("inverse", inverse)
#
#bcd - last in dist
# print(dist[len(dist)-1])
# #3 - number of appearences of bcd
# print(dict.get((len(dist)-1),num))
# #last and number: bcd 3
# print(dist[len(dist)-1], dict.get((len(dist)-1),num))
#another way
popular_word = max(set(s), key=s.count)
print(popular_word, s.count(popular_word))
