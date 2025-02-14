"""
https://www.acmicpc.net/problem/14592
"""

print(
    sorted(
        [list(map(int, input().split())) + [i + 1] for i in range(int(input()))],
        key=lambda x: (-x[0], x[1], x[2])
    )[0][3]
)
