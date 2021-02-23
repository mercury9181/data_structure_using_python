fivonacci_cache = dict()
def fiv(n):
    if n in fivonacci_cache:
        return fivonacci_cache[n]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        value = fiv(n-1)+fiv(n-2)
        fivonacci_cache[n] = value
        return value


n= int(input("enter number= "))
for i in range(0,n):
    print(fiv(i), end=' ')