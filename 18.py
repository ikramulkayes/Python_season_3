times = int(input())
lst = []
finalsum = ""
for elm in range(times):
    m = input()
    m = int(m)
    klst = []
    for kelm in range(m+1):
        if kelm == 0:
            yoyo = input()
        else:
            l = input()
            klst.append(l)
    finalcypher = yoyo.split()
    count = 0
    #finalsum = ""
    for elm in klst:
        elm = elm.split()
        elm = elm[1]
        cypher = int(finalcypher[count])
        for k in elm:
            if k == "U":
                if cypher ==0:
                    cypher =9
                else:
                    cypher -=1
            else:
                if cypher ==9:
                    cypher =0
                else:
                    cypher +=1
            #print(cypher)
        count += 1
        finalsum += str(cypher)+" "
    finalsum = finalsum.rstrip()
    finalsum += "\n"
finalsum = finalsum.rstrip("\n")
print(finalsum)



