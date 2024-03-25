def check(n):
	if n==0:
		return "zero"
	elif n<0:
		return "negative"
	else:
		return "positive"
def oe(n):
	if n%2==0:
		return "even"
	else:
		return "odd"
num=10
print(num,"is",check(num))
print(num,"is",oe(num))