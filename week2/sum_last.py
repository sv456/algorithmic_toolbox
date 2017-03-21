#python2
def sum_fib(n):
    a=list()
    a.append(0)
    a.append(1)
    if n<=1:
        return n
    i=2
    while i<=n:
        a.append((a[i-1]+a[i-2])%10)
        if a[i]==1 and a[i-1]==0:
            break
        i+=1
    if n>60:
        a.pop()
    res=sum(a)%10
    su=0
    if (float(n)/60)>1:
        m=n//60
        res=res*m
        c=m*60
        if n-c!=0:
            j=0
            for k in a:
                if j<=n-c:
                    su+=k
                j+=1
                
    return (res+su)%10
    
if __name__=='__main__':
    num=int(raw_input())
    print sum_fib(num)
