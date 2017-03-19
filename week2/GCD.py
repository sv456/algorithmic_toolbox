def gcd(a,b):
	if b==0:
		return a
	while True:
		rem=a%b
		if rem==0:
			break
		a=b
		b=rem
		
	return b

a=int(raw_input("enter value:"))
b=int(raw_input("enter value less than a:"))
print gcd(a,b)
