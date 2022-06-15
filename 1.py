


times = int(input())
blst = []
for elm in range(times):
    #m = input()
    k = int(input())
    blst.append(k)
for elm in blst:
    #print(elm)
    s = elm//3
    #print(s)
    mid = s 
    big = s 
    small = s
    if elm%2 ==0:
        flag = True
    else:
        flag = False
    if flag == False:
        mid += 1
        big += 2
        small -= 1
    else:
        big += 1
        small -= 1
    
    

    
        


    

    print(f"{mid} {big} {small}")

    
