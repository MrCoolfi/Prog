def split(a,b):
    res = [[] for i in range(b)]
    for i in range(len(a)):
        res[i%b].append(a[i])
    return(res)

if __name__ == '__main__':
    print(split([1,2,3,4,5],2))