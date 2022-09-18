times = int(input())
lst = []
for elm in range(times):
    k = input()
    lst.append(int(k))
diglst = [0,1,2,3,4,5,6,7,8,9]
diglst= diglst[::-1]
#print(diglst)
for elm in lst:
    sum1 = 0
    strsum1 = ""
    for i in diglst:
        if (i+sum1) <= elm:
            sum1 += i
            strsum1 += str(i)
        if sum1 == elm:
            break
    print(strsum1[::-1])
        
            

