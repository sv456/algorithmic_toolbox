def fib_fast(n):
    a=list()
    a.append(0)
    a.append(1)
    if n<=1:
        return n
    i=2
    while i<=n:
        a.append(a[i-1]+a[i-2])
        i+=1
    return a[n]
