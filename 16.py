times = int(input())
lst = []
for elm in range(times):
    k = input()
    lst.append(k)
for elm in lst:
    if elm.lower() == "yes":
        print("YES")
    else:
        print("NO")
