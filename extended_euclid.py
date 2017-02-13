def extended_gcd(x,y):
	if y == 0:
		return (x, 1, 0)
	else:
		(d, a, b) = extended_gcd(y, x % y)
		return (d, b, a - x//y * b)

print("a (mod b)")
x = int(input("Enter a. \t"))
y = int(input("Enter b. \t"))
print(extended_gcd(x,y)[1])