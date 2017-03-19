#python2

n=int(raw_input())
if n>=2 and n<=200000:
    a=[int(x) for x in raw_input().split()]
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
                if i>largest:
                    sec_largest=largest
                    largest=i
                elif largest > i and i>sec_largest:
                    sec_largest=i


        print largest*sec_largest
