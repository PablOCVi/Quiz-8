def find_threes(x):
	sum=0
	for y in x:
		if (y%3==0):
			sum=sum+y
	return sum
y=[0,4,2,6,9,8,3,12]

print(find_threes(y))