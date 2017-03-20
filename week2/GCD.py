#python2
def gcd(a,b):
        if a>=b:
                if b==0:
                        return a
                while True:
                        rem=a%b
                        if rem==0:
                                break
                        a=b
                        b=rem
                        
                return b
        else:
                if a==0:
                        return b
                while True:
                        rem=b%a
                        if rem==0:
                                break
                        b=a
                        a=rem
                        
                return a

if __name__=='__main__':
        num=[int(x) for x in raw_input().split()]
        a=num[0]
        b=num[1]
        print gcd(a,b)
