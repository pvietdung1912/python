ds=[0.3,0.4,0.6,0.9,0.12,0.22]
def median(ds):
	if len(ds)%2==0:
		tv=(ds[len(ds)//2-1]+ds[len(ds)//2+1])
	else:
		tv=ds[len(ds)//2]
	return tv;
tv=median(ds)
print(tv)