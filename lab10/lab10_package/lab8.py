def f3(arg):
    def f1(min, max):

        def f2(val):
            val = int(val)
            if min <= val <= max:
                return 'Good'
            else:
                return 'Bad'

        return f2
    x = f1(10,30)
    return x(arg)
