"""
https://www.acmicpc.net/problem/8958
"""

from collections import deque

T = int(input())

for _ in range(T):
    q = deque(list(input()))
    score = 0
    o_count = 0

    while q:
        answer = q.popleft()
        o_count = o_count + 1 if answer == "O" else 0
        score += o_count * 1

    print(score)
