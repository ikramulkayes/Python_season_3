times = int(input())
lst = []
for elm in range(times):
    m = input()
    k = input()
    lst.append(k)
for elm in lst:
    sum1 = 0
    lst = []
    for selm in elm:
        if selm not in lst:
            sum1 += 2
            lst.append(selm)
        else:
            sum1 += 1
    print(sum1)
