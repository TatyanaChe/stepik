# lst = [int(i) for i in input().split()]
# x=int(input())
# if x in lst:
# #     for i in [i for i,b in enumerate(lst) if b == x]:
# #         print(i, end=" ")
#     [print(i, end=" ") for i, b in enumerate(lst) if b == x]
# else: print("Отсутствует")
#
# lst = [int(i) for i in input().split()]
# x=int(input())
# if x in lst:
# #     for i in [i for i,b in enumerate(lst) if b == x]:
# #         print(i, end=" ")
#     [print(i, end=" ") for i, b in enumerate(lst) if b == x]
# else: print("Отсутствует")
#
a = []
sec=[]
summa = 0
while True:
    a = int(input())
    summa = summa + a
    pow2 = pow(a,2)
    sec.append(pow2)
    if summa == 0:
            break
i=0
sumsec=0
for i in range(len(sec)):
    sumsec=sumsec + sec[i]
    i+=1
print(sumsec)