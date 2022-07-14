times = int(input())
lst = []
finalsum = ""
for elm in range(times):
    m = input()
    m = int(m)
    klst = []
    for kelm in range(m):

            l = input()
            klst.append(l)
    count = 0
    flag = False
    for elm in klst:
        flag = False
        for kelm in klst:
            for melm in klst:
                if (kelm + melm) == elm:
                    finalsum += "1"
                    flag = True
                    break
            if flag:
                break
        if flag == False:
            finalsum += "0"
    finalsum += "\n"
finalsum = finalsum.rstrip("\n")
print(finalsum)
            
        