def fibonacci(n):
	if n<=1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)
num=5
print("sequences:")
for i in range(num):
	print(fibonacci(num)