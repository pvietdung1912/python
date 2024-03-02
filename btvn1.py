n=int(input('please enter a positive number n:'))
def giaithua(n):
	gt=1
	while n!=0:
		gt=gt*n
		n=n-1
	return gt;
print('n giai thua bang:',giaithua(n))