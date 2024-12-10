"""
https://www.acmicpc.net/problem/11279
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for j in range(m):
    if arr[0][j] == "1":
        dp[0][j] = 1
        
for i in range(1, n):
    if arr[i][0] == "1":
        dp[i][0] = 1

    for j in range(1, m):
        if arr[i][j] == "1":
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

max_num = 0
for i in range(n):
    for j in range(m):
        max_num = max(max_num, dp[i][j])

print(max_num ** 2)