"""
https://www.acmicpc.net/problem/2845
"""

import sys

input = sys.stdin.readline

L, P = map(int, input().split())

news_list = list(map(int, input().split()))

result = []

for news in news_list:
    result.append(str(int(news) - L * P))

print(" ".join(result))
