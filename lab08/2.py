def f1(f):

    def f2(a,b):
        try:
            return f(a,b)
        except Exception as e:
            print('Ошибка',e)
    return f2

@f1
def del1(x,y):
    return x/y


print(del1(10,2))
print(del1(10,0))