"""
https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test
"""

from collections import deque

K, N = map(int, input().split())

dq = deque()
dq.append(N)

max_num = 200000
visited = [0] * (max_num + 1)
visited_c = [0] * (max_num + 1)
visited_c[N] = K

is_catch = False

while dq:
    x = dq.popleft()

    if x == visited_c[x]:
        print(visited[x])
        is_catch = True
        break

    for i in (x + 1, x - 1, x * 2):
        if 0 <= i <= max_num and not visited[i]:
            visited[i] = visited[x] + 1
            visited_c[i] = visited_c[x] + visited[x] + 1
            dq.append(i)

if not is_catch:
    print(-1)
