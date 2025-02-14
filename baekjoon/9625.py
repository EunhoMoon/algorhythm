"""
https://www.acmicpc.net/problem/9625
"""

K = int(input())

count_A, count_B = 0, 1

for _ in range(2, K + 1):
    count_A, count_B = count_B, count_A + count_B

print(f"{count_A} {count_B}")
