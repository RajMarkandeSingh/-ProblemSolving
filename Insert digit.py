t = int(input())
for i in range(t):
	n, d = input().split()
	n = int(n)
	S = list(input())
	for j in range(n):
		if d > S[j]:
			S.insert(j, d)
			break
	if len(S) == n:
		S.append(d)
	print("".join(S))
