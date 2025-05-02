def compute(num):
    if num==0:
        return []
    def tup(num):
        def sqr(num,rep=2):
            if rep==0:
                return 1
            return num*sqr(num,rep-1)
        def cube(num,rep=3):
            if rep==0:
                return 1
            return num*cube(num,rep-1)
        return (num,sqr(num),cube(num))
    return [tup(num)]+compute(num-1)

print(compute(5))      
