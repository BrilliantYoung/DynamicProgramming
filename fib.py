def fib(n):
	Fib=[]
	for i in range(n+1):
		if i==0 or i==1:
			Fib.append(i)
		else:
			Fib.append(Fib[i-1]+Fib[i-2])
	return Fib

if __name__ == '__main__':
	n = 10
	ans = fib(n)
	print(ans)