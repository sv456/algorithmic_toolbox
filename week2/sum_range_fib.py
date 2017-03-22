#As sum of 60 consecutive fibonacci series is 0 we can trim input so take m % 60 and n % 60, so now the range is reduced
#python2
def sum_fib(m,n):
    if m>n:
        return
    a=[0,1]
    for i in xrange(2,60):
        a.append(a[i-1]+a[i-2])

    m=m%60
    n=n%60
    if n<m:
        n+=60
    su=0
    for j in xrange(m,n+1):
        su+=a[j]

    return su%10
    
if __name__=='__main__':
    num=[int(x) for x in raw_input().split()]
    print sum_fib(num[0],num[1])
