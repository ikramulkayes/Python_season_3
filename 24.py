times = int(input())
lst = []
for elm in range(times):
    k = input()
    m = input().split()
    

    lst.append(m)
for belm in lst:
    fst = len(belm)
    #temp = belm.copy()
    #count = 0
    for i in range(fst):
        temp = belm[i::]
        #print(temp)

        exlst = []
        for elm in temp:
            if elm not in exlst:
                exlst.append(elm)
        if len(exlst) == len(temp):
            break
        #print(sum1)
    print(i)
    


