"""
https://www.acmicpc.net/problem/2422
"""

N, M = map(int, input().split())

icecreams = [i for i in range(1, N + 1)]
ignored = set()
count = 0

for _ in range(M):
    a, b = map(int, input().split())
    ignored.add((a, b))
    ignored.add((b, a))

for i in range(1, N - 1):
    for j in range(i + 1, N):
        if (i, j) in ignored:
            continue
        for k in range(j + 1, N + 1):
            if (i, k) not in ignored and (j, k) not in ignored:
                count += 1

print(count)
