# Uses python2
import sys

def get_change(m):
    #write your code here
    change_list=[10,5,1]
    sum=0
    n=m
    cnt=0
    for i in change_list:
        while sum<m:
            if i<=n:
                sum+=i
                n=n-i
                cnt+=1
            else:
                break
        if sum==m:
            break
       
            
    return cnt

if __name__ == '__main__':
    m = int(raw_input())
    print get_change(m)
