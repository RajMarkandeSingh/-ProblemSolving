cur, res = 1, 1
N = int(input())
arr = list(map(int, input().split()))
for i in range(1, N):
    if arr[i] >= arr[i-1]:
        cur += 1
        res = max(cur, res)
    else:
        cur = 1
print(res)
