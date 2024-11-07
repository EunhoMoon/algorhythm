"""
https://www.acmicpc.net/problem/1181
"""

import sys

input = sys.stdin.readline

N = int(input())
words = set()

for _ in range(N):
    words.add(input().strip())

words_list = list(words)
words_list.sort()
words_list.sort(key=lambda x: len(x))

for word in words_list:
    print(word)
