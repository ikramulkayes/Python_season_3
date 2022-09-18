f = [5,5,15,9,8,6,2]
x = [45,55,65,75,85,95,105]
totalsum = 0
for elm in range(len(f)):
    #sum1 = f[elm]*x[elm]
    sum1 = f[elm]*f[elm]
    print(sum1)
    totalsum+=sum1
print(totalsum)