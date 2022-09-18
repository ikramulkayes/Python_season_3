times = int(input())
lst = []
for elm in range(times):
    k = input().split()
    ktimes = int(k[0])
    smlast = [k]
    #print(smlast)
    for mm in range(ktimes):
        k = input().split()
        #print(k)
        smlast.append(k)
        #print(smlast)


    lst.append(smlast)
#print(lst)
for belm in lst:
    headlst = belm[0]
    times = int(headlst[0])
    headlst = headlst[1::]
    alarms = belm[1::]
    minhour = None
    minhourlst = None
    for elm in alarms:
        hour = int(elm[0])
        if minhour ==None:
            minhour = hour
            minhourlst = elm
    finalhour = int(headlst)


