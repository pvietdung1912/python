n=int(input('please enter a positive number n:'))
def tb(n):
	sum=0
	i=0
	while True :
		if (n<0):
			break
		if (n%2==0):
			sum=sum+n
			i=i+1
		n=int(input('please enter a positive number n:'))
	return float(sum/i);
print('trung binh cac so chan vua nhap la',tb(n))