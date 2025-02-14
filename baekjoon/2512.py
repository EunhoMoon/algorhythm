"""
https://www.acmicpc.net/problem/2512
"""

import sys

read_line = sys.stdin.readline

N = int(read_line())
request_budgets = list(map(int, read_line().split()))
M = int(read_line())

left, right = 0, max(request_budgets)
result = 0

while left <= right:
    mid = (left + right) // 2
    total = sum(min(budget, mid) for budget in request_budgets)

    if total <= M:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
