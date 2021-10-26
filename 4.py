n = int(input())
First = [int(i) for i in input().split()]
Second = [int(i) for i in input().split()]
h = First[0] + Second[0]
for k in range(1, n):
	if (First[k] + Second[k]) > h:
		h = First[k] + Second[k]
Gist = [[0]*n for i in range(h)]
for i in range(n):
	F = First[i]
	S = Second[i]
	B = h - (F + S)
	for j1 in range(F):
		ind = (h - 1) - j1
		Gist[ind][i] = '#'
	for j2 in range(S):
		ind = (h - 1 - F) - j2
		Gist[ind][i] = '*'
	if B != 0:
		for j3 in range(B):
			ind = (B - 1) - j3
			Gist[ind][i] = '.'
for i in range(h):
	if i != 0:
		print('')
	for j in range(n):
		print(Gist[i][j], end = '')
print(' ')