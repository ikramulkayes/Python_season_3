

times = int(input())
firstlst = []
lst = []
for elm in range(times):
    m = input()
    firstlst.append(m.split())
    k = input()
    lst.append(k.split())
for i in range(times):
    a = firstlst[i][0]
    b = lst[i]
    elm = []
    for k in b:
        k = int(k)
        elm.append(k)
    elm = sorted(elm)
    count = 0
    flag = True
    for k in elm:
        if count ==0:
            prev = k
            count += 1
        else:
            sum1 = k - prev
            if sum1 <= 0:
                flag = False
                break
            else:
                prev = k
    if flag:
        print("YES")
    else:
        print("NO")
