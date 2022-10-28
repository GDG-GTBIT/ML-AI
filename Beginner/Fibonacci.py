def  fibonacci(n):

	if n == 1  or n == 0:

		return n;

	else:

		return fibonacci(n-2) + fibonacci(n - 1)


num = int(input("Enter number of digits: "))

if num < 0:
	print("Not valid")

i = 0

print("Fibonacci series is")

for i in range(0, num):
	print(fibonacci(i))