n = int(input())
a = int(input())
b = int(input())
pol = n//2
if a <= pol:
	Sanya = a 
	Kolya = n - a 
elif b <= pol:
	Kolya = b
	Sanya = n - b 
else:
	if n%2 == 0:
		Sanya = pol
		Kolya = pol
	else:
		Sanya = pol + 1
		Kolya = pol
print(Sanya, Kolya)