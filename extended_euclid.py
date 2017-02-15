def extended_gcd(x,y):
	if y == 0:
		return (x, 1, 0)
	else:
		(d, a, b) = extended_gcd(y, x % y)
		return (d, b, a - x//y * b)

print("Find a^-1 in (mod b)")
x = int(input("Enter a *the value to be inverted*. \t"))
y = int(input("Enter b *the modular base*. \t"))
answer = extended_gcd(x,y)[1]
if answer < 0:
	answer += y 
print("Inverse to " + str(x) + " in mod " + str(y) + " is " + str(answer) + ".") 
