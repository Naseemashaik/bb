m,n=map(int,raw_input().split())
for j in range(m+1,n):
	if(j>1):
		for i in range(2,j):
			if(j%i==0):
				break
                        else:
                         	print j,
