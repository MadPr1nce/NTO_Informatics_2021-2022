n = int(input())
a = [int(i) for i in input().split()]
y2 = a[0]
high = 0
low = 0
for i in range(1, n):
	y1 = y2
	y2 = a[i]
	if y1 > y2:
		continue
	else:
		if y1 > 2000 and y2 > 2000:
			high += (y2 - y1)
		elif y1 < 2000 and y2 < 2000:
			low += (y2 - y1)
		else:
			high += (y2 - 2000)
			low += (2000 - y1)
print (low, high)