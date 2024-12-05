"""
https://www.acmicpc.net/problem/10610
"""

N = input().strip()


def is_multiple_of_30(num_string: str) -> bool:
    if "0" not in num_string or sum(map(int, list(num_string))) % 3 > 0:
        return False
    else:
        return True


if is_multiple_of_30(N):
    print("".join(sorted(list(N), reverse=True)))
else:
    print(-1)
