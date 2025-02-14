"""
https://www.acmicpc.net/problem/2435
"""

import sys
from collections import deque

input = sys.stdin.readline

# 도화지 초기화
paper = [[False] * 100 for _ in range(100)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
result = 0

# 색종이 위치 초기화
for _ in range(int(input())):
    left, bottom = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[bottom + i][left + j] = True

# 완전탑색
for y in range(100):
    for x in range(100):
        if paper[y][x]:
            for k in range(4):
                ny, nx = y + dy[k], x + dx[k]
                # 인접한 영역이 흰색이(not paper[ny][nx])거나 도화지의 경계(100 <= 위치 < 0)일 경우 둘레 증가
                if ny < 0 or ny >= 100 or nx < 0 or nx >= 100 or not paper[ny][nx]:
                    result += 1

print(result)
