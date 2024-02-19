sum=0
n=int(input('please enter a positive number n:'))
while (n!=0):
	if (n%2!=0):
		sum=sum+n
	n=int(input('please enter a positive number n:'))
print('tong cua cac so le vua nhap la',sum)