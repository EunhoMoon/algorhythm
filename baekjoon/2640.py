"""
https://www.acmicpc.net/problem/2630
"""

import sys

input = sys.stdin.readline

N = int(input())
papper = []
count_blue = count_white = 0

for _ in range(N):
    papper.append(list(map(int, input().split())))


def split_papper(pappers: list[list[int]], length: int):
    global count_blue, count_white
    for papper in pappers:
        is_true = True
        prev_color = 2
        for i in range(length):
            for j in range(length):
                if prev_color < 2 and prev_color != papper[i][j]:
                    is_true = False
                    break
                prev_color = papper[i][j]
            if not is_true:
                break
        if is_true:
            if prev_color:
                count_blue += 1
            else:
                count_white += 1
        else:
            new_pappers = get_new_pappers(papper)
            split_papper(new_pappers, len(papper) // 2)


def get_new_pappers(papper):
    length = len(papper)
    new_length = length // 2
    new_pappers = []
    for row_start in range(0, length, new_length):
        for col_start in range(0, length, new_length):
            new_papper = [
                row[col_start : col_start + new_length]
                for row in papper[row_start : row_start + new_length]
            ]
            new_pappers.append(new_papper)
    return new_pappers


split_papper([papper], N)

print(count_white)
print(count_blue)
