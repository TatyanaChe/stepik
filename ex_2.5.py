# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
# print(students)
#
# a = [int(i) for i in input().split()]
# sum=0
# j=0
# for j in range(len(a)):
#     sum+=a[j]
#     j+=1
# print(sum)
# a = [int(i) for i in input().split()]
# sum=0
# j=0
# endSum=[]
# if (len(a)==1):
#     print(a[0])
# for j in range(len(a)-1):
#     sum=(a[j-1] + a[j+1])
#     endSum.append(sum)
#     j+=1
#     if j==(len(a)-1):
#         sum=(a[j-1] + a[0])
#         endSum.append(sum)
# print(*endSum)
#
# a = [int(i) for i in input().split()]
# orderedA= sorted(a)
# distinct= []
# distinct.append(orderedA[0])
# i=1
# for i in range(len(orderedA)):
#     if orderedA[i] not in distinct:
#         distinct.append(orderedA[i])
#     i+=1
# print(distinct)
#
a = [int(i) for i in input().split()]
orderedA= sorted(a)
distinct= []
i=0
for i in range(len(orderedA)):
    if orderedA[i] not in distinct:
        sum=orderedA.count(orderedA[i])
        if sum>=2:
            distinct.append(orderedA[i])
    i+=1
print(*distinct)