def split(b):
    b = int(b)
    res = [[] for i in range(b)]
    for i in range(len([1,2,3,4,5,6,7,8,9,10])):
        res[i%b].append([1,2,3,4,5,6,7,8,9,10][i])
    return(res)



