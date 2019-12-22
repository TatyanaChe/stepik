# X=int(input())
# Hours=X//60
# Minutes=X%60
# X=int(input())
# print(X//60)
# print(X%60)
# #
# X=int(input())
# H=int(input())
# M=int(input())
# print((X+H*60+M)//60)
# print((X+H*60+M)%60)

# print(*divmod(int(input()), 60), sep='\n')
#
# a,b = True, False
# c=((a and b) or ((not a) and (not b)))
# print(c)
#
# x = 5
# y = 10
# print(y > x * x or y >= 2 * x and x < y)

a = True
b = False
c=(a and b or not a and not b)
print(c)