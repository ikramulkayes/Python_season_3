def solve(n):
    maxsum = None
    maxsumval = None
    for elm in range(n+1):
        elm = str(elm)
        sum1 = 0
        for selm in elm:
            sum1 += int(selm)
        if maxsum == None:
            maxsum = sum1
            maxsumval = elm
        elif sum1 >= maxsum:
            maxsum = sum1
            maxsumval = elm
        
        #print(maxsumval)
    return int(maxsumval)

print(solve(48))