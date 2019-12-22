# i = 0
# print("first i ",i)
# while i <= 10:
#     i = i + 1
#     print("i in while ", i)
#     if i > 7:
#         i = i + 2
#         print("i in if ", i)

# n = int(input())
# c = 1
# while c <= n:
#     print('*' * c)
#     c += 1
#
# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1
#
# a = int(input())
# b = int(input())
# s = 0
# i = a
# while i <= b:
#     s += i
#     i += 1
# print(s)
#
# a = 30
# b = 18
# # NOD by division
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
# print("NOD by division", a + b)
#NOD by subtraction
# a = 30
# b = 18
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
# print("NOD by subtraction ", a)
# NOD by division #2
# a = 30
# b = 18
# a,b = (int(input()) for i in range(2))
# a,b=(int(input()) for i in range(2))
# c=a*b
# print("a*b= ", c)
# while b != 0:
#    a, b = b, a % b
# # print("NOD by division #2 ", a)
# #
# NOD=a
# print("NOD= ", NOD)
# NOK=int(c/NOD)
# print("NOK= ", NOK)

# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     # print(i)
#     s = s + i
#     if s > 15:
#         break
#     i = i + 1
#     # print(i)
# print(i)
#
# i = 0
# s = 0
# while i < 10:
#     i = i + 1
#     s = s + i
#     if s > 15:
#         continue
#     i = i + 1
# print(i)
#
# a=0
# while (a<101):
#     a=int(input())
#     # print("a=", a )
#     if a<10:
#         # print("a<10")
#         continue
#     elif a>=101:
#         # print("a>100")
#         break
#     else:
#         print(a)
#
# a,b,c,d=int(input()) in range(4)
a=2
b=4
c=2
d=4
for i in range(a,b+1):
    print(i*c,i*d,sep="\t")