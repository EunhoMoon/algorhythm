"""
https://www.acmicpc.net/problem/15874
"""

import sys

input = sys.stdin.readline

upper = [ord("A"), ord("Z")]
lower = [ord("a"), ord("z")]

k, s = map(int, input().split())

origin_str = input().strip()
new_str: str = ""

k = k % 26


def parshing(char, k, range) -> int:
    return (
        ord(char) + k
        if ord(char) + k <= range[1]
        else ord(char) + k - (range[1] - range[0] + 1)
    )


for char in origin_str:
    new_char = char
    if upper[0] <= ord(char) <= upper[1]:
        new_char = chr(parshing(char=char, k=k, range=upper))
    elif lower[0] <= ord(char) <= lower[1]:
        new_char = chr(parshing(char=char, k=k, range=lower))

    new_str += new_char

print(new_str)
