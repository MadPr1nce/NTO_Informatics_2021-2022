k, n = (int(i) for i in input().split())
Code = [str(i) for i in input().split()]
Summ = 2**n 
black_list = set()
for i in Code:
	m = len(i)
	if m > n:
		Vr = int(i)
		Vr //= int((10**(m-n)))
		black_list.add(Vr)
k = len(Code)
for i in range(k):
	m = len(Code[i])
	Vychet = n - m
	if Vychet > 0:
		Summ -= (2**Vychet)
	elif Vychet == 0:
		Summ -= 1
k = len(black_list)
print(Summ - k)