"""
https://www.acmicpc.net/problem/1620
 - 시간 복잡도를 줄이기 위해 index 조회는 list, 이름 조회는 dict
"""
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pokemon_list = []
pokemon_dict = {}

for idx in range(1, N + 1):
    name = input().rstrip()
    pokemon_list.append(name)
    pokemon_dict[name] = idx

for _ in range(M):
    command = input().rstrip()
    print(
        pokemon_list[int(command) - 1] if command.isdigit() else pokemon_dict[command]
    )
