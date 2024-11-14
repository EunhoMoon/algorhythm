"""
https://www.acmicpc.net/problem/1764
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

d = []
b = []
for idx in range(n + k):
    name = input().replace("\n", "")
    if idx < n:
        d.append(name)
    else:
        b.append(name)

result = sorted(list(set(d).intersection(set(b))))

print(len(result))
for name in result:
    print(name)
