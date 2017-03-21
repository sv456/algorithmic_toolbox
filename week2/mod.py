#python2
def modulo(n,m):
    period=n+1
    a=list()
    a.append(0)
    a.append(1)
    a.append(1)
    if n<=1:
        return n
    i=3
    while i<=n:
        a.append((a[i-1]+a[i-2])%m)
        if(a[i]==1 and a[i-1]==0):
            period=i-1
            break
        i+=1

    index=n%period
    rem=a[index]
    return rem

if __name__=='__main__':
    num=[int(x) for x in raw_input().split()]
    n=num[0]
    m=num[1]
    print modulo(n,m)
