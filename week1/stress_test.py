#python2
import random

def pro_fast(n,a):
    for i in a:
        if i>=0 and i<=100000:
            flag=True
        else:
            flag=False
            break
    if flag is True:
        if len(a)==n:
            largest=0
            sec_largest=0
            for i in a:
                if i>=largest:
                    sec_largest=largest
                    largest=i
                elif largest >= i and i>=sec_largest:
                    sec_largest=i


        return largest*sec_largest

def pro(n,a):
    for i in a:
        if i>=0 and i<=100000:
            flag=True
        else:
            flag=False
            break
    res=0
    if flag is True:
        if len(a)==n:
            for i in range(0,n):
                for j in range(i+1,n):
                    if a[i]*a[j]>res:
                        res=a[i]*a[j]

    return res


if __name__=='__main__':
    while True:
        num=random.randrange(2,20001)
        print 'num',num
        a=list()
        i=0
        while i<num:
            a.append(random.randrange(0,10001))
            i+=1
        res1=pro_fast(num,a)
        res2=pro(num,a)
        if res1!=res2:
            print 'o/p wrong res1:',res1,' res2:',res2
            break
        else:
            print 'ok'
