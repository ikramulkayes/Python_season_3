def two_sum(numbers, target):
    flag = None
    for elm in range(len(numbers)):
        prev = numbers[elm]
        #print(prev)
        for selm in range(elm+1,len(numbers)):
            #print(selm)
            sum1 = prev + numbers[selm]
            #print(sum1)
            if sum1 == target:
                return [elm,selm]
#better way

def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]

print(two_sum([2,2,3], 4))


            


            


