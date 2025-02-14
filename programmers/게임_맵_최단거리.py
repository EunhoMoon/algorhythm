from collections import deque


def is_valid_croods(a, b, n, m):
    return 0 <= a < n and 0 <= b < m


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dy = (1, 0, -1, 0)
    dx = (0, 1, 0, -1)
    dq = deque()
    dq.append((0, 0, 1))
    chk = [[False] * m for _ in range(n)]

    while dq:
        y, x, count = dq.popleft()

        if y == n - 1 and x == m - 1:
            return count

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if is_valid_croods(ny, nx, n, m) and not chk[ny][nx] and maps[ny][nx]:
                chk[ny][nx] = True
                dq.append((ny, nx, count + 1))

    return -1
