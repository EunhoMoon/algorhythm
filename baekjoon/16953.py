"""
https://www.acmicpc.net/problem/16953
"""

from collections import deque
import math

A, B = map(int, input().split())

dq = deque()
dq.append((A, 1))

min_count = math.inf

while dq:
    num, count = dq.popleft()

    if num == B:
        min_count = min(min_count, count)

    new_nums = [num * 2, int(f"{num}1")]
    for new_num in new_nums:
        if new_num <= B:
            dq.append((new_num, count + 1))

print(min_count if min_count < math.inf else -1)
