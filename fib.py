def fib1(a):
	if a<=1:
		return a
	return fib1(a-1) + fib1(a-2)

def fib2(l):
	a = 0
	b = 1
	c = None
	print("Fibonacci series is : 0 1 ",end="")
	for i in range(l - 2):
		c = a + b
		a = b
		b = c
		print(b , end = " ")

l = int(input("Enter th length of fibanacci series : "))
ch = input("Enter 1 -> fib1() || Enter 2 -> fib2(l) : ")
if ch=='1':
	print("Fib series is : ",end="")
	for i in range(l):
		print(fib1(i) , end=" ")
else:
	fib2(l)
