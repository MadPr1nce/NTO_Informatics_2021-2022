n, m = (int(i) for i in input().split())
box = []
for i in range(1, m):
	box += [n*i]
	for j in range(1, n):
		box += [(n*i) + (m - i)*j]
for i in range(1, n):
	box += [m*i]
	for j in range(1, m):
		box += [(m*i) + (n - i)*j]
BOX = sorted(box)
print( BOX[0], end=' ')
k = len(BOX)
for l in range(1, k):
	if BOX[l] == BOX[l-1]:
		continue
	else:
		print(BOX[l], end=' ')