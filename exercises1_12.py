# a=int(input())
# b=int(input())
# c=int(input())
# a,b,c=(int(input()) for i in range(3))
# p=(a+b+c)/2
# print((p*(p-a)*(p-b)*(p-c))**0.5)
# print(S)
#
# a = int(input())
# if ((-15<a<=12) or (14<a<17) or a>=19):
#     print("True")
# else: print("False")

# a,b=(float(input()) for i in range(2))
# c=str(input())
# if (c=='+'):
#     print(a+b)
# elif (c=="-"):
#     print(a-b)
# elif (c=="*"):
#     print(a*b)
# elif (c=="pow"):
#     print(a ** b)
# if (b==0 and (c=="/" or c=="mod" or c=="div")):
#     print("Деление на 0!")
# if (c=="/" and b!=0):
#     print(a/b)
# elif (c=="mod" and b!=0):
#     print(a%b)
# elif (c=="div" and b!=0):
#     print(a//b)
#
# figure=input()
# if figure=="прямоугольник":
#     a, b = (float(input()) for i in range(2))
#     print(a*b)
# elif figure=="треугольник":
#     a, b, c = (float(input()) for i in range(3))
#     p = (a + b + c) / 2
#     print(((p*(p-a)*(p-b)*(p-c))**0.5))
# elif figure == "круг":
#     a = float(input())
#     print((a**2)*3.14)
#
# a,b,c=(int(input()) for i in range(3))
# max = max(a,b,c)
# min = min(a,b,c)
# sum = a+b+c
# rest = sum-(max+min)
# print(str(max) +'\n' + str(min) + '\n'+ str(rest))
#
# if a < b:
# 	a, b = b, a
# if a < c:
# 	a, c = c, a
# if b > c:
# 	b, c = c, b
# print(a)
# print(b)
# print(c)
#
# number=0
# while number<1000:
# number = input()
# stringN=str(number)
# last = stringN[-1]
# twolast = stringN[-2:]
# n= int(last)
# word="программист"
# if (twolast == '11' or twolast == '12' or twolast == '13' or twolast == '14'):
#     print(number, word + "ов")
# else:
#     if (n==0 or n>=5):
#         print(number, word + "ов")
#     if n == 1:
#         print(number, word)
#     if (2 <=n<= 4):
#         print(number,word + "а")
#     # number+=1
#
# strTicket = input()
# threeFirst = strTicket[0:3]
# firstLeft=int(threeFirst[0])
# secondLeft=int(threeFirst[1])
# thirdLeft=int(threeFirst[2])
# sumLeft=firstLeft+secondLeft+thirdLeft
# print("sumLeft", sumLeft)
# threeLast = strTicket[-3:]
# firstRight=int(threeLast[-3])
# secondRight=int(threeLast[-2])
# thirdRight=int(threeLast[-1])
# sumRight=firstRight+secondRight+thirdRight
# print("sumRight", sumRight)
# if (sumLeft==sumRight): print("Счастливый")
# else: print("Обычный")
#
a, b, c, d, e, f = input()
n= int(a)+int (b)+int(c)
m= int(d)+int (e)+int(f)
if n==m:
    print ('Счастливый')
else:
    print ('Обычный')