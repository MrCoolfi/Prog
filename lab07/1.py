def split(a,b):
    res = [[] for i in range(b)]
    for i in range(len(a)):
        res[i%b].append(a[i])
    return(res)

print(split([1,2,3,4,5],2))
print(split([1,2,3,4,5],3))
print(split([1,2,3,4,5],4))
print(split([1,2,3,4,5],5))
