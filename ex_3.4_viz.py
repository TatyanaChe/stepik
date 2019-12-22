s='a3e10b1'
print(s)
#
for i in range(len(s)-1):
    print("i= ", i)
    if s[i].isalpha():
        if ((s[i+1]).isdigit()):
            num = s[i + 1]
            if i<len(s)-2:
                if (s[i+2]).isdigit():
                    num = s[i+1] + s[i+2]
            num=str(s[i]) * (int(num))
            print("num=", num)
        i+= 1
    else:
        i+=1