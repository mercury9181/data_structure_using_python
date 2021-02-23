def fiv(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fiv(n-1)+fiv(n-2)


n= int(input("enter number= "))
for i in range(0,n):
    print(fiv(i), end=' ')