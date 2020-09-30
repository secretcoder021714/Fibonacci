#fibonacci_approach
#this is a recursive approach
def fib(a):
	if a<=1:
		return a
	return fib(a-1) + fib(a-2)

#main code
l = int(input("Enter th length of fibanacci series : "))
print("Fib series is : ",end="")
for i in range(l):
	print(fib(i) , end=" ")
