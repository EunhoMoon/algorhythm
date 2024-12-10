"""
https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test
"""

from collections import deque

cony, brown = map(int, input().split())

dq = deque()
dq.append(brown)

max_position = 200000
brown_visited = [0] * (max_position + 1)
cony_visited = [0] * (max_position + 1)
cony_visited[brown] = cony

is_failed = True

while dq:
    brown_position = dq.popleft()
    cony_position = cony_visited[brown_position]

    if cony_position > max_position:
        break

    if brown_position == cony_position:
        print(brown_visited[brown_position])
        is_failed = False
        break

    for i in (brown_position + 1, brown_position - 1, brown_position * 2):
        if 0 <= i <= max_position and not brown_visited[i]:
            brown_visited[i] = brown_visited[brown_position] + 1
            cony_visited[i] = (
                cony_visited[brown_position] + brown_visited[brown_position] + 1
            )
            dq.append(i)

if is_failed:
    print(-1)
