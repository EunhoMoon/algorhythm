"""
https://www.acmicpc.net/problem/1676
"""

import math

N = int(input())

n_fact = list(str(math.factorial(N)))
count = 0

for i in range(len(n_fact) - 1, 0, -1):
    if n_fact[i] == "0":
        count += 1
    else:
        break

print(count)
