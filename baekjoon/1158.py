"""
https://www.acmicpc.net/problem/1158
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

people: list = list(range(1, n + 1))
result: list = []
idx = 0

while people:
    idx = (idx + k - 1) % len(people)
    # idx + k - 1: 건너 뛰어야 할 사람 수
    # % len(people): 총 사람 수를 넘기지 않도록 순환 구조 모방
    result.append(str(people.pop(idx)))

print("<" + ", ".join(result) + ">")
