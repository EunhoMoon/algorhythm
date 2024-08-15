"""
https://www.acmicpc.net/problem/1966
"""

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())

    documents = list(map(int, input().split()))
    PQ = sorted(documents, reverse=True)

    queue = [(idx, value) for idx, value in enumerate(documents)]
    num = 1

    while queue:
        k, v = queue[0]
        if PQ[0] == v:
            if k == M:
                print(num)
                break
            PQ = PQ[1:]
            num += 1
        else:
            queue.append(queue[0])

        queue = queue[1:]
